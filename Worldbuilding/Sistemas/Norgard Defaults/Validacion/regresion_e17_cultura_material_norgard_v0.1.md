# Regresión E17 — cultura material común de Norgard v0.1

## Estado esperado

**NORGARD_DEFAULT_E17_MATERIAL_CULTURE_POINT_13_COMPATIBLE**

## Invariantes

1. Point 13 defines a shared technological baseline, not identical regional styling.
2. Norgard remains preindustrial.
3. Electricity is not part of ordinary Norgard material culture.
4. Internal combustion engines are absent.
5. Steam industry is absent.
6. Factory mechanization is not assumed.
7. Industrial mass production is not assumed.
8. Industrial interchangeable parts are not assumed.
9. Modern piped domestic water is not assumed.
10. Mechanical clocks do not exist.
11. Tower clocks do not exist.
12. Pocket watches do not exist.
13. Wristwatches do not exist.
14. Civil water clocks are not a normal timekeeping system.
15. Civil hourglass clocks are not a normal timekeeping system.
16. TIME may know exact time even if characters cannot.
17. Bells may signal events but are not clocks.
18. Hourly bell schedules are not assumed.
19. A common urban sundial network is not assumed.
20. Wood is a common structural and object material.
21. Stone is a common durable building material.
22. Slate may be used where supply exists.
23. Iron exists and is common enough for selected tools and hardware.
24. Steel exists for selected edges or high-performance pieces.
25. Steel is not cheap and universal.
26. Copper and compatible alloys may exist without universal abundance.
27. Gold and silver are not ordinary household construction materials.
28. Ceramic vessels are common.
29. Glass exists but is limited and relatively costly.
30. Large modern glass windows are not ordinary.
31. Rope is a common material resource.
32. Wool is a common textile fibre.
33. Linen is a common textile fibre.
34. Leather is common.
35. Hide and fur may exist where appropriate.
36. Cotton is not a common Norgard textile.
37. Silk is not a common Norgard textile.
38. Natural dyes exist.
39. Exact dye plants are not invented by Point 13.
40. Optical-modern white clothing is not assumed.
41. Industrial standard clothing sizes are absent.
42. Clothing remains a persistent material good.
43. A humble household may own functional furniture.
44. A humble household is not automatically broken, empty or filthy.
45. Wealth may increase furniture quantity and quality.
46. Wealth does not unlock a later technological era.
47. Beds exist but modern sprung mattresses do not.
48. Chests and coffers are common storage options.
49. Sacks, baskets, barrels and jars are normal storage options.
50. A container must physically exist to contain goods.
51. Simple metal locks exist.
52. Not every door has a lock.
53. Bars, latches and bolts remain valid closures.
54. Possessing a key does not grant ownership or permission.
55. Simple kitchen pots exist.
56. Iron cauldrons and pans may exist.
57. Kitchen knives exist.
58. Wooden spoons and ladles exist.
59. Mortars and pestles exist.
60. Full modern cutlery sets are not assumed.
61. Personal knives may serve at table.
62. Buckets and basins exist.
63. Simple soap exists.
64. Simple soap does not imply modern detergent.
65. Perfumed soap is not universally cheap.
66. Cleaning may use hot water, ash, friction and brushing.
67. Small mirrors may be polished metal or costlier reflective glass.
68. Large modern mirrors are not assumed.
69. Daylight is the primary light source when available.
70. Tallow candles exist as ordinary artificial light.
71. Beeswax candles exist at higher cost.
72. Simple lamps/candils may exist.
73. Torches are not default indoor domestic lighting.
74. Artificial light consumes fuel/material.
75. Open flame participates in FIRE risk.
76. Writing by hand exists.
77. Parchment exists.
78. Paper exists.
79. Paper is not assumed free or disposable.
80. Quills and ink exist.
81. Sealing wax and seals may exist.
82. Manuscript books exist.
83. Account books exist.
84. Industrial printing is absent.
85. Copying a book requires material, labour and time.
86. Physical archives require storage and protection.
87. Documents do not become public knowledge merely by existing.
88. Carpentry tools are manual.
89. Axes, adzes, saws, chisels and planes may exist.
90. Agricultural tools are manual or animal-powered.
91. Ploughs do not imply engines.
92. Forges require fuel and equipment.
93. Smithing uses anvils, hammers, tongs and bellows.
94. Spindles exist.
95. Spinning wheels may exist.
96. Hand looms may exist.
97. Industrial looms are absent.
98. Construction may use plumb lines, simple pulleys and wooden scaffolds.
99. Transport may use carts and wagons.
100. Vehicles require human or animal power.
101. Vehicles require roads/terrain compatibility.
102. Vehicles wear and need maintenance.
103. Ordinary healer material may include cloth, splints, needles and containers.
104. Modern syringes are absent.
105. Thermometers are absent.
106. Stethoscopes are absent.
107. Industrial sterile kits are absent.
108. Regional variation affects frequency, finish, material and imports.
109. Valrik may emphasize high-quality woodwork.
110. Galdren may emphasize agricultural material culture.
111. Darovan may show more trade/imported goods where supplied.
112. Edranor may emphasize wine-production material culture.
113. Hallheim may concentrate high craft and multi-region goods.
114. Great Houses do not have different technological ages.
115. Catalog entries authorize possibility but do not spawn objects.
116. Object ownership remains under OWN.
117. Object condition remains under COND.
118. Tools remain under TOOL and WS.
119. Locks and access remain under DOOR.
120. Buildings remain under BUILD.
121. Discarded objects/material remain under WASTE where applicable.
122. Fire risk remains under FIRE.
123. AI may describe compatible canonical objects.
124. AI may not invent modern technology.
125. AI may not create an object merely by describing it.
126. AI may not introduce a clock.
127. AI may not ignore ownership or condition.
128. LOD may aggregate ordinary object capacity.
129. Unique/relevant objects may be promoted to persistent identity.
130. Promotion of an object does not reroll its history.
131. Point 13 closes shared material culture without freezing future regional aesthetics.

## Regla de regresión

Debe fallar cualquier implementación que introduzca relojes, tecnología industrial/moderna, objetos sin cadena material, riqueza equivalente a modernidad, inventario que ignore OWN/COND/TOOL/DOOR o que fuerce a todas las regiones a compartir el mismo estilo visual.

Marcador esperado:

`MATERIAL_CULTURE_POINT_13_CLOSED_NORGARD_SHARED_MATERIAL_CULTURE`
