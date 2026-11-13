#include <array>
#include <filesystem>
#include <iostream>
#include <corerpg/content_json/content_catalog_loader.hpp>
#include <corerpg/definition_id.hpp>
#include <corerpg/world_state.hpp>
#include <corerpg/random_streams.hpp>
#include <corerpg/persistence.hpp>
int main(int argc,char**argv) {
  if(argc!=2)return 1;
  const std::array<std::filesystem::path,1> roots{std::filesystem::path{argv[1]}};
  const auto loaded=corerpg::content_json::load_content_catalog(roots);
  if(!loaded.succeeded() || !loaded.catalog())return 2;
  const auto* catalog=loaded.catalog();
  if(catalog->size()!=5)return 3;
  constexpr std::array<const char*,5> ids{
    "nimroel.edranor.territory:territory/edranor",
    "nimroel.edranor.territory:places/dorth",
    "nimroel.edranor.territory:places/lumina",
    "nimroel.edranor.territory:places/karsath",
    "nimroel.edranor.territory:places/rodas"};
  for(auto id:ids)if(!catalog->find_by_value(id))return 4;
  // TEST_ONLY: synthetic state, never a playable or canon population.
  corerpg::WorldState world;
  if(world.entity_count()!=0)return 5;
  const auto e=world.create_entity();
  const auto f=world.create_entity();
  const auto dorth=corerpg::DefinitionId::parse(ids[1]);
  const auto rodas=corerpg::DefinitionId::parse(ids[4]);
  if(!dorth || !rodas || !e.is_valid() || !f.is_valid())return 6;
  if(world.bind_definition(e,*catalog,*dorth)!=corerpg::DefinitionBindingChange::applied)return 7;
  if(world.bind_definition(f,*catalog,*rodas)!=corerpg::DefinitionBindingChange::applied)return 8;
  corerpg::RandomStreams random{110011};
  const auto data=corerpg::Persistence::serialize(corerpg::Persistence::capture(world,random));
  if(data.status!=corerpg::PersistenceStatus::success)return 9;
  corerpg::WorldState restored;
  corerpg::RandomStreams rng2{99};
  if(corerpg::Persistence::load(data.bytes,restored,rng2,{},catalog)!=corerpg::PersistenceStatus::success)return 10;
  if(restored.entity_count()!=2 || !restored.definition_of(e) ||
     restored.definition_of(e)->value()!=ids[1] || !restored.definition_of(f) ||
     restored.definition_of(f)->value()!=ids[4])return 11;
  corerpg::WorldState replay;
  const auto replay_e=replay.create_entity();
  const auto replay_f=replay.create_entity();
  if(replay.bind_definition(replay_e,*catalog,*dorth)!=corerpg::DefinitionBindingChange::applied ||
     replay.bind_definition(replay_f,*catalog,*rodas)!=corerpg::DefinitionBindingChange::applied)return 12;
  corerpg::RandomStreams same_seed{110011};
  const auto replay_data=corerpg::Persistence::serialize(corerpg::Persistence::capture(replay,same_seed));
  if(replay_data.status!=corerpg::PersistenceStatus::success || replay_data.bytes!=data.bytes)return 13;
  corerpg::WorldState missing_catalog;
  corerpg::RandomStreams rng3{99};
  const auto rejection=corerpg::Persistence::load(data.bytes,missing_catalog,rng3);
  if(rejection!=corerpg::PersistenceStatus::catalog_required || missing_catalog.entity_count()!=0)return 14;
  std::cout<<"EDRANOR_E11_CORE_CPP_OK catalog=5 TEST_ONLY_entities=2 save_restore=1 same_seed_bytes=1 missing_catalog_rejected=1\n";
  return 0;
}
