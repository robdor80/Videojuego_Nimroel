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
    "nimroel.darovan.territory:territory/darovan",
    "nimroel.darovan.territory:cities/treihord",
    "nimroel.darovan.territory:cities/veldora",
    "nimroel.darovan.territory:cities/taramin",
    "nimroel.darovan.territory:cities/syvaris"};
  for(auto id:ids)if(!catalog->find_by_value(id))return 4;
  // Laboratorio TEST_ONLY: nunca inserta personajes en partidas ni en canon.
  corerpg::WorldState world;
  if(world.entity_count()!=0)return 5;
  const auto e=world.create_entity();
  const auto id=corerpg::DefinitionId::parse(ids[1]);
  if(!id || !e.is_valid())return 6;
  if(world.bind_definition(e,*catalog,*id)!=corerpg::DefinitionBindingChange::applied)return 7;
  corerpg::RandomStreams random{110011};
  auto data=corerpg::Persistence::serialize(corerpg::Persistence::capture(world,random));
  if(data.status!=corerpg::PersistenceStatus::success)return 8;
  corerpg::WorldState restored;
  corerpg::RandomStreams rng2{99};
  if(corerpg::Persistence::load(data.bytes,restored,rng2,{},catalog)!=corerpg::PersistenceStatus::success)return 9;
  if(restored.entity_count()!=1 || !restored.definition_of(e) || restored.definition_of(e)->value()!=ids[1])return 10;
  std::cout<<"DAROVAN_D11_CORE_CPP_OK catalog=5 TEST_ONLY_save_restore=1\n";
  return 0;
}
