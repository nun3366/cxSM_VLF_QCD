# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 12.3.1 for Microsoft Windows (64-bit) (June 24, 2021)
# Date: Wed 19 Oct 2022 16:38:23


from object_library import all_vertices, all_CTvertices, Vertex, CTVertex
import particles as P
import CT_couplings as C
import lorentz as L


V_1 = CTVertex(name = 'V_1',
               type = 'R2',
               particles = [ P.g, P.g, P.g ],
               color = [ 'f(1,2,3)' ],
               lorentz = [ L.VVV1, L.VVV2, L.VVV4, L.VVV6, L.VVV7, L.VVV8 ],
               loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.g] ] ],
               couplings = {(0,0,0):C.R2GC_343_156,(0,0,1):C.R2GC_343_157,(0,1,0):C.R2GC_346_158,(0,1,1):C.R2GC_346_159,(0,2,0):C.R2GC_346_158,(0,2,1):C.R2GC_346_159,(0,3,0):C.R2GC_343_156,(0,3,1):C.R2GC_343_157,(0,4,0):C.R2GC_343_156,(0,4,1):C.R2GC_343_157,(0,5,0):C.R2GC_346_158,(0,5,1):C.R2GC_346_159})

V_2 = CTVertex(name = 'V_2',
               type = 'R2',
               particles = [ P.g, P.g, P.g, P.g ],
               color = [ 'd(-1,1,3)*d(-1,2,4)', 'd(-1,1,3)*f(-1,2,4)', 'd(-1,1,4)*d(-1,2,3)', 'd(-1,1,4)*f(-1,2,3)', 'd(-1,2,3)*f(-1,1,4)', 'd(-1,2,4)*f(-1,1,3)', 'f(-1,1,2)*f(-1,3,4)', 'f(-1,1,3)*f(-1,2,4)', 'f(-1,1,4)*f(-1,2,3)', 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
               lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
               loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.g] ] ],
               couplings = {(2,0,0):C.R2GC_256_93,(2,0,1):C.R2GC_256_94,(0,0,0):C.R2GC_256_93,(0,0,1):C.R2GC_256_94,(6,0,0):C.R2GC_259_98,(6,0,1):C.R2GC_354_166,(4,0,0):C.R2GC_254_89,(4,0,1):C.R2GC_254_90,(3,0,0):C.R2GC_254_89,(3,0,1):C.R2GC_254_90,(8,0,0):C.R2GC_255_91,(8,0,1):C.R2GC_255_92,(7,0,0):C.R2GC_260_100,(7,0,1):C.R2GC_353_165,(5,0,0):C.R2GC_254_89,(5,0,1):C.R2GC_254_90,(1,0,0):C.R2GC_254_89,(1,0,1):C.R2GC_254_90,(11,0,0):C.R2GC_258_96,(11,0,1):C.R2GC_258_97,(10,0,0):C.R2GC_258_96,(10,0,1):C.R2GC_258_97,(9,0,1):C.R2GC_257_95,(2,1,0):C.R2GC_256_93,(2,1,1):C.R2GC_256_94,(0,1,0):C.R2GC_256_93,(0,1,1):C.R2GC_256_94,(4,1,0):C.R2GC_254_89,(4,1,1):C.R2GC_254_90,(3,1,0):C.R2GC_254_89,(3,1,1):C.R2GC_254_90,(8,1,0):C.R2GC_255_91,(8,1,1):C.R2GC_352_164,(6,1,0):C.R2GC_350_161,(6,1,1):C.R2GC_350_162,(7,1,0):C.R2GC_260_100,(7,1,1):C.R2GC_260_101,(5,1,0):C.R2GC_254_89,(5,1,1):C.R2GC_254_90,(1,1,0):C.R2GC_254_89,(1,1,1):C.R2GC_254_90,(11,1,0):C.R2GC_258_96,(11,1,1):C.R2GC_258_97,(10,1,0):C.R2GC_258_96,(10,1,1):C.R2GC_258_97,(9,1,1):C.R2GC_257_95,(2,2,0):C.R2GC_256_93,(2,2,1):C.R2GC_256_94,(0,2,0):C.R2GC_256_93,(0,2,1):C.R2GC_256_94,(4,2,0):C.R2GC_254_89,(4,2,1):C.R2GC_254_90,(3,2,0):C.R2GC_254_89,(3,2,1):C.R2GC_254_90,(8,2,0):C.R2GC_255_91,(8,2,1):C.R2GC_349_160,(6,2,0):C.R2GC_259_98,(6,2,1):C.R2GC_259_99,(7,2,0):C.R2GC_351_163,(7,2,1):C.R2GC_256_94,(5,2,0):C.R2GC_254_89,(5,2,1):C.R2GC_254_90,(1,2,0):C.R2GC_254_89,(1,2,1):C.R2GC_254_90,(11,2,0):C.R2GC_258_96,(11,2,1):C.R2GC_258_97,(10,2,0):C.R2GC_258_96,(10,2,1):C.R2GC_258_97,(9,2,1):C.R2GC_257_95})

V_3 = CTVertex(name = 'V_3',
               type = 'R2',
               particles = [ P.u__tilde__, P.d, P.G__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               loop_particles = [ [ [P.d, P.g, P.u] ] ],
               couplings = {(0,0,0):C.R2GC_372_179,(0,1,0):C.R2GC_373_180})

V_4 = CTVertex(name = 'V_4',
               type = 'R2',
               particles = [ P.c__tilde__, P.d, P.G__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               loop_particles = [ [ [P.c, P.d, P.g] ] ],
               couplings = {(0,0,0):C.R2GC_308_130,(0,1,0):C.R2GC_307_129})

V_5 = CTVertex(name = 'V_5',
               type = 'R2',
               particles = [ P.u__tilde__, P.s, P.G__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               loop_particles = [ [ [P.g, P.s, P.u] ] ],
               couplings = {(0,0,0):C.R2GC_375_182,(0,1,0):C.R2GC_376_183})

V_6 = CTVertex(name = 'V_6',
               type = 'R2',
               particles = [ P.c__tilde__, P.s, P.G__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               loop_particles = [ [ [P.c, P.g, P.s] ] ],
               couplings = {(0,0,0):C.R2GC_324_141,(0,1,0):C.R2GC_323_140})

V_7 = CTVertex(name = 'V_7',
               type = 'R2',
               particles = [ P.t__tilde__, P.b, P.G__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS4 ],
               loop_particles = [ [ [P.b, P.g, P.t] ] ],
               couplings = {(0,0,0):C.R2GC_339_151,(0,1,0):C.R2GC_340_152})

V_8 = CTVertex(name = 'V_8',
               type = 'R2',
               particles = [ P.d__tilde__, P.d, P.G0 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               loop_particles = [ [ [P.d, P.g] ] ],
               couplings = {(0,0,0):C.R2GC_301_123})

V_9 = CTVertex(name = 'V_9',
               type = 'R2',
               particles = [ P.s__tilde__, P.s, P.G0 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               loop_particles = [ [ [P.g, P.s] ] ],
               couplings = {(0,0,0):C.R2GC_317_134})

V_10 = CTVertex(name = 'V_10',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.G0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_279_109})

V_11 = CTVertex(name = 'V_11',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.H3 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_303_125})

V_12 = CTVertex(name = 'V_12',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.H3 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_319_136})

V_13 = CTVertex(name = 'V_13',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.H3 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_280_110})

V_14 = CTVertex(name = 'V_14',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.H2 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_304_126})

V_15 = CTVertex(name = 'V_15',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.H2 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_320_137})

V_16 = CTVertex(name = 'V_16',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.H2 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_281_111})

V_17 = CTVertex(name = 'V_17',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_305_127})

V_18 = CTVertex(name = 'V_18',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_321_138})

V_19 = CTVertex(name = 'V_19',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_282_112})

V_20 = CTVertex(name = 'V_20',
                type = 'R2',
                particles = [ P.d__tilde__, P.u, P.G__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.d, P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_366_173,(0,1,0):C.R2GC_363_170})

V_21 = CTVertex(name = 'V_21',
                type = 'R2',
                particles = [ P.s__tilde__, P.u, P.G__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.g, P.s, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_367_174,(0,1,0):C.R2GC_364_171})

V_22 = CTVertex(name = 'V_22',
                type = 'R2',
                particles = [ P.d__tilde__, P.c, P.G__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.c, P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_300_122,(0,1,0):C.R2GC_302_124})

V_23 = CTVertex(name = 'V_23',
                type = 'R2',
                particles = [ P.s__tilde__, P.c, P.G__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.c, P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_316_133,(0,1,0):C.R2GC_318_135})

V_24 = CTVertex(name = 'V_24',
                type = 'R2',
                particles = [ P.b__tilde__, P.t, P.G__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.b, P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_334_146,(0,1,0):C.R2GC_332_144})

V_25 = CTVertex(name = 'V_25',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.G0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_365_172})

V_26 = CTVertex(name = 'V_26',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.G0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_289_116})

V_27 = CTVertex(name = 'V_27',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.G0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_333_145})

V_28 = CTVertex(name = 'V_28',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.H3 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_368_175})

V_29 = CTVertex(name = 'V_29',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.H3 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_290_117})

V_30 = CTVertex(name = 'V_30',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.H3 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_335_147})

V_31 = CTVertex(name = 'V_31',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.H2 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_369_176})

V_32 = CTVertex(name = 'V_32',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.H2 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_291_118})

V_33 = CTVertex(name = 'V_33',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.H2 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_336_148})

V_34 = CTVertex(name = 'V_34',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_370_177})

V_35 = CTVertex(name = 'V_35',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_292_119})

V_36 = CTVertex(name = 'V_36',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_337_149})

V_37 = CTVertex(name = 'V_37',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_263_104})

V_38 = CTVertex(name = 'V_38',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_263_104})

V_39 = CTVertex(name = 'V_39',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_263_104})

V_40 = CTVertex(name = 'V_40',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_261_102})

V_41 = CTVertex(name = 'V_41',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_261_102})

V_42 = CTVertex(name = 'V_42',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_261_102})

V_43 = CTVertex(name = 'V_43',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_262_103})

V_44 = CTVertex(name = 'V_44',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_262_103})

V_45 = CTVertex(name = 'V_45',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_262_103})

V_46 = CTVertex(name = 'V_46',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_262_103})

V_47 = CTVertex(name = 'V_47',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_262_103})

V_48 = CTVertex(name = 'V_48',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_262_103})

V_49 = CTVertex(name = 'V_49',
                type = 'R2',
                particles = [ P.d__tilde__, P.u, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.d, P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_359_168})

V_50 = CTVertex(name = 'V_50',
                type = 'R2',
                particles = [ P.s__tilde__, P.u, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.g, P.s, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_360_169})

V_51 = CTVertex(name = 'V_51',
                type = 'R2',
                particles = [ P.d__tilde__, P.c, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.c, P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_297_121})

V_52 = CTVertex(name = 'V_52',
                type = 'R2',
                particles = [ P.s__tilde__, P.c, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.c, P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_313_132})

V_53 = CTVertex(name = 'V_53',
                type = 'R2',
                particles = [ P.b__tilde__, P.t, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.b, P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_329_143})

V_54 = CTVertex(name = 'V_54',
                type = 'R2',
                particles = [ P.u__tilde__, P.d, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.d, P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_371_178})

V_55 = CTVertex(name = 'V_55',
                type = 'R2',
                particles = [ P.c__tilde__, P.d, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.c, P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_306_128})

V_56 = CTVertex(name = 'V_56',
                type = 'R2',
                particles = [ P.u__tilde__, P.s, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.g, P.s, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_374_181})

V_57 = CTVertex(name = 'V_57',
                type = 'R2',
                particles = [ P.c__tilde__, P.s, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.c, P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_322_139})

V_58 = CTVertex(name = 'V_58',
                type = 'R2',
                particles = [ P.t__tilde__, P.b, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.b, P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_338_150})

V_59 = CTVertex(name = 'V_59',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_287_114,(0,1,0):C.R2GC_288_115})

V_60 = CTVertex(name = 'V_60',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_287_114,(0,1,0):C.R2GC_288_115})

V_61 = CTVertex(name = 'V_61',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_287_114,(0,1,0):C.R2GC_288_115})

V_62 = CTVertex(name = 'V_62',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_277_107,(0,1,0):C.R2GC_278_108})

V_63 = CTVertex(name = 'V_63',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_277_107,(0,1,0):C.R2GC_278_108})

V_64 = CTVertex(name = 'V_64',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_277_107,(0,1,0):C.R2GC_278_108})

V_65 = CTVertex(name = 'V_65',
                type = 'R2',
                particles = [ P.u__tilde__, P.u ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1, L.FF2, L.FF3, L.FF4 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_358_167,(0,2,0):C.R2GC_358_167,(0,1,0):C.R2GC_273_105,(0,3,0):C.R2GC_273_105})

V_66 = CTVertex(name = 'V_66',
                type = 'R2',
                particles = [ P.c__tilde__, P.c ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1, L.FF2, L.FF3, L.FF4 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_286_113,(0,2,0):C.R2GC_286_113,(0,1,0):C.R2GC_273_105,(0,3,0):C.R2GC_273_105})

V_67 = CTVertex(name = 'V_67',
                type = 'R2',
                particles = [ P.t__tilde__, P.t ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1, L.FF2, L.FF3, L.FF4 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_328_142,(0,2,0):C.R2GC_328_142,(0,1,0):C.R2GC_273_105,(0,3,0):C.R2GC_273_105})

V_68 = CTVertex(name = 'V_68',
                type = 'R2',
                particles = [ P.d__tilde__, P.d ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1, L.FF2, L.FF3, L.FF4 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_296_120,(0,2,0):C.R2GC_296_120,(0,1,0):C.R2GC_273_105,(0,3,0):C.R2GC_273_105})

V_69 = CTVertex(name = 'V_69',
                type = 'R2',
                particles = [ P.s__tilde__, P.s ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1, L.FF2, L.FF3, L.FF4 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_312_131,(0,2,0):C.R2GC_312_131,(0,1,0):C.R2GC_273_105,(0,3,0):C.R2GC_273_105})

V_70 = CTVertex(name = 'V_70',
                type = 'R2',
                particles = [ P.b__tilde__, P.b ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1, L.FF2, L.FF3, L.FF4 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_276_106,(0,2,0):C.R2GC_276_106,(0,1,0):C.R2GC_273_105,(0,3,0):C.R2GC_273_105})

V_71 = CTVertex(name = 'V_71',
                type = 'R2',
                particles = [ P.g, P.g ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VV1, L.VV2, L.VV3 ],
                loop_particles = [ [ [P.b] ], [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                couplings = {(0,0,4):C.R2GC_342_155,(0,1,0):C.R2GC_235_5,(0,1,2):C.R2GC_235_6,(0,1,3):C.R2GC_235_7,(0,1,5):C.R2GC_235_8,(0,1,6):C.R2GC_235_9,(0,1,7):C.R2GC_235_10,(0,2,1):C.R2GC_341_153,(0,2,4):C.R2GC_341_154})

V_72 = CTVertex(name = 'V_72',
                type = 'R2',
                particles = [ P.g, P.g, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVS1 ],
                loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_242_31,(0,0,1):C.R2GC_242_32,(0,0,2):C.R2GC_242_33,(0,0,3):C.R2GC_242_34,(0,0,4):C.R2GC_242_35,(0,0,5):C.R2GC_242_36})

V_73 = CTVertex(name = 'V_73',
                type = 'R2',
                particles = [ P.g, P.g, P.H2 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVS1 ],
                loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_241_25,(0,0,1):C.R2GC_241_26,(0,0,2):C.R2GC_241_27,(0,0,3):C.R2GC_241_28,(0,0,4):C.R2GC_241_29,(0,0,5):C.R2GC_241_30})

V_74 = CTVertex(name = 'V_74',
                type = 'R2',
                particles = [ P.g, P.g, P.H3 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVS1 ],
                loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_240_19,(0,0,1):C.R2GC_240_20,(0,0,2):C.R2GC_240_21,(0,0,3):C.R2GC_240_22,(0,0,4):C.R2GC_240_23,(0,0,5):C.R2GC_240_24})

V_75 = CTVertex(name = 'V_75',
                type = 'R2',
                particles = [ P.a, P.g, P.g, P.Z ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.VVVV7 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_236_11,(0,0,1):C.R2GC_236_12})

V_76 = CTVertex(name = 'V_76',
                type = 'R2',
                particles = [ P.g, P.g, P.Z, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVVV7 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_239_17,(0,0,1):C.R2GC_239_18})

V_77 = CTVertex(name = 'V_77',
                type = 'R2',
                particles = [ P.g, P.g, P.W__minus__, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVVV7 ],
                loop_particles = [ [ [P.b, P.t] ], [ [P.c, P.d] ], [ [P.c, P.s] ], [ [P.d, P.u] ], [ [P.s, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_250_79,(0,0,1):C.R2GC_250_80,(0,0,2):C.R2GC_250_81,(0,0,3):C.R2GC_250_82,(0,0,4):C.R2GC_250_83})

V_78 = CTVertex(name = 'V_78',
                type = 'R2',
                particles = [ P.a, P.a, P.g, P.g ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVVV7 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_233_1,(0,0,1):C.R2GC_233_2})

V_79 = CTVertex(name = 'V_79',
                type = 'R2',
                particles = [ P.g, P.g, P.g, P.Z ],
                color = [ 'd(1,2,3)', 'f(1,2,3)' ],
                lorentz = [ L.VVVV1, L.VVVV7 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(1,0,0):C.R2GC_238_15,(1,0,1):C.R2GC_238_16,(0,1,0):C.R2GC_237_13,(0,1,1):C.R2GC_237_14})

V_80 = CTVertex(name = 'V_80',
                type = 'R2',
                particles = [ P.a, P.g, P.g, P.g ],
                color = [ 'd(2,3,4)' ],
                lorentz = [ L.VVVV7 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_234_3,(0,0,1):C.R2GC_234_4})

V_81 = CTVertex(name = 'V_81',
                type = 'R2',
                particles = [ P.g, P.g, P.H, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_249_73,(0,0,1):C.R2GC_249_74,(0,0,2):C.R2GC_249_75,(0,0,3):C.R2GC_249_76,(0,0,4):C.R2GC_249_77,(0,0,5):C.R2GC_249_78})

V_82 = CTVertex(name = 'V_82',
                type = 'R2',
                particles = [ P.g, P.g, P.G0, P.G0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_243_37,(0,0,1):C.R2GC_243_38,(0,0,2):C.R2GC_243_39,(0,0,3):C.R2GC_243_40,(0,0,4):C.R2GC_243_41,(0,0,5):C.R2GC_243_42})

V_83 = CTVertex(name = 'V_83',
                type = 'R2',
                particles = [ P.g, P.g, P.G__minus__, P.G__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.b, P.t] ], [ [P.c, P.d] ], [ [P.c, P.s] ], [ [P.d, P.u] ], [ [P.s, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_251_84,(0,0,1):C.R2GC_251_85,(0,0,2):C.R2GC_251_86,(0,0,3):C.R2GC_251_87,(0,0,4):C.R2GC_251_88})

V_84 = CTVertex(name = 'V_84',
                type = 'R2',
                particles = [ P.g, P.g, P.H, P.H2 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_248_67,(0,0,1):C.R2GC_248_68,(0,0,2):C.R2GC_248_69,(0,0,3):C.R2GC_248_70,(0,0,4):C.R2GC_248_71,(0,0,5):C.R2GC_248_72})

V_85 = CTVertex(name = 'V_85',
                type = 'R2',
                particles = [ P.g, P.g, P.H2, P.H2 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_246_55,(0,0,1):C.R2GC_246_56,(0,0,2):C.R2GC_246_57,(0,0,3):C.R2GC_246_58,(0,0,4):C.R2GC_246_59,(0,0,5):C.R2GC_246_60})

V_86 = CTVertex(name = 'V_86',
                type = 'R2',
                particles = [ P.g, P.g, P.H, P.H3 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_247_61,(0,0,1):C.R2GC_247_62,(0,0,2):C.R2GC_247_63,(0,0,3):C.R2GC_247_64,(0,0,4):C.R2GC_247_65,(0,0,5):C.R2GC_247_66})

V_87 = CTVertex(name = 'V_87',
                type = 'R2',
                particles = [ P.g, P.g, P.H2, P.H3 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_245_49,(0,0,1):C.R2GC_245_50,(0,0,2):C.R2GC_245_51,(0,0,3):C.R2GC_245_52,(0,0,4):C.R2GC_245_53,(0,0,5):C.R2GC_245_54})

V_88 = CTVertex(name = 'V_88',
                type = 'R2',
                particles = [ P.g, P.g, P.H3, P.H3 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_244_43,(0,0,1):C.R2GC_244_44,(0,0,2):C.R2GC_244_45,(0,0,3):C.R2GC_244_46,(0,0,4):C.R2GC_244_47,(0,0,5):C.R2GC_244_48})

V_89 = CTVertex(name = 'V_89',
                type = 'UV',
                particles = [ P.g, P.g, P.g ],
                color = [ 'f(1,2,3)' ],
                lorentz = [ L.VVV1, L.VVV2, L.VVV3, L.VVV4, L.VVV5, L.VVV6, L.VVV7, L.VVV8 ],
                loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                couplings = {(0,0,0):C.UVGC_343_146,(0,0,1):C.UVGC_343_147,(0,0,2):C.UVGC_343_148,(0,0,3):C.UVGC_343_149,(0,0,4):C.UVGC_253_4,(0,0,5):C.UVGC_343_150,(0,0,6):C.UVGC_343_151,(0,0,7):C.UVGC_343_152,(0,1,0):C.UVGC_346_157,(0,1,1):C.UVGC_346_158,(0,1,2):C.UVGC_346_159,(0,1,3):C.UVGC_346_160,(0,1,4):C.UVGC_346_161,(0,1,5):C.UVGC_346_162,(0,1,6):C.UVGC_346_163,(0,1,7):C.UVGC_346_164,(0,3,0):C.UVGC_346_157,(0,3,1):C.UVGC_346_158,(0,3,2):C.UVGC_346_159,(0,3,3):C.UVGC_348_167,(0,3,4):C.UVGC_252_2,(0,3,5):C.UVGC_346_162,(0,3,6):C.UVGC_346_163,(0,3,7):C.UVGC_346_164,(0,5,0):C.UVGC_343_146,(0,5,1):C.UVGC_343_147,(0,5,2):C.UVGC_343_148,(0,5,3):C.UVGC_345_155,(0,5,4):C.UVGC_345_156,(0,5,5):C.UVGC_343_150,(0,5,6):C.UVGC_343_151,(0,5,7):C.UVGC_343_152,(0,6,0):C.UVGC_343_146,(0,6,1):C.UVGC_343_147,(0,6,2):C.UVGC_343_148,(0,6,3):C.UVGC_344_153,(0,6,4):C.UVGC_344_154,(0,6,5):C.UVGC_343_150,(0,6,6):C.UVGC_343_151,(0,6,7):C.UVGC_343_152,(0,7,0):C.UVGC_346_157,(0,7,1):C.UVGC_346_158,(0,7,2):C.UVGC_346_159,(0,7,3):C.UVGC_347_165,(0,7,4):C.UVGC_347_166,(0,7,5):C.UVGC_346_162,(0,7,6):C.UVGC_346_163,(0,7,7):C.UVGC_346_164,(0,2,3):C.UVGC_252_1,(0,2,4):C.UVGC_252_2,(0,4,3):C.UVGC_253_3,(0,4,4):C.UVGC_253_4})

V_90 = CTVertex(name = 'V_90',
                type = 'UV',
                particles = [ P.g, P.g, P.g, P.g ],
                color = [ 'd(-1,1,3)*d(-1,2,4)', 'd(-1,1,3)*f(-1,2,4)', 'd(-1,1,4)*d(-1,2,3)', 'd(-1,1,4)*f(-1,2,3)', 'd(-1,2,3)*f(-1,1,4)', 'd(-1,2,4)*f(-1,1,3)', 'f(-1,1,2)*f(-1,3,4)', 'f(-1,1,3)*f(-1,2,4)', 'f(-1,1,4)*f(-1,2,3)', 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
                loop_particles = [ [ [P.b] ], [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                couplings = {(2,0,4):C.UVGC_255_8,(2,0,5):C.UVGC_255_7,(0,0,4):C.UVGC_255_8,(0,0,5):C.UVGC_255_7,(6,0,0):C.UVGC_353_194,(6,0,2):C.UVGC_353_195,(6,0,3):C.UVGC_353_196,(6,0,4):C.UVGC_354_202,(6,0,5):C.UVGC_354_203,(6,0,6):C.UVGC_353_199,(6,0,7):C.UVGC_353_200,(6,0,8):C.UVGC_353_201,(4,0,4):C.UVGC_254_5,(4,0,5):C.UVGC_254_6,(3,0,4):C.UVGC_254_5,(3,0,5):C.UVGC_254_6,(8,0,4):C.UVGC_255_7,(8,0,5):C.UVGC_255_8,(7,0,0):C.UVGC_353_194,(7,0,2):C.UVGC_353_195,(7,0,3):C.UVGC_353_196,(7,0,4):C.UVGC_353_197,(7,0,5):C.UVGC_353_198,(7,0,6):C.UVGC_353_199,(7,0,7):C.UVGC_353_200,(7,0,8):C.UVGC_353_201,(5,0,4):C.UVGC_254_5,(5,0,5):C.UVGC_254_6,(1,0,4):C.UVGC_254_5,(1,0,5):C.UVGC_254_6,(11,0,4):C.UVGC_258_11,(11,0,5):C.UVGC_258_12,(10,0,4):C.UVGC_258_11,(10,0,5):C.UVGC_258_12,(9,0,4):C.UVGC_257_9,(9,0,5):C.UVGC_257_10,(2,1,4):C.UVGC_255_8,(2,1,5):C.UVGC_255_7,(0,1,4):C.UVGC_255_8,(0,1,5):C.UVGC_255_7,(4,1,4):C.UVGC_254_5,(4,1,5):C.UVGC_254_6,(3,1,4):C.UVGC_254_5,(3,1,5):C.UVGC_254_6,(8,1,0):C.UVGC_352_186,(8,1,2):C.UVGC_352_187,(8,1,3):C.UVGC_352_188,(8,1,4):C.UVGC_352_189,(8,1,5):C.UVGC_352_190,(8,1,6):C.UVGC_352_191,(8,1,7):C.UVGC_352_192,(8,1,8):C.UVGC_352_193,(6,1,0):C.UVGC_350_176,(6,1,2):C.UVGC_350_177,(6,1,3):C.UVGC_350_178,(6,1,4):C.UVGC_350_179,(6,1,5):C.UVGC_350_180,(6,1,6):C.UVGC_350_181,(6,1,7):C.UVGC_350_182,(6,1,8):C.UVGC_350_183,(7,1,1):C.UVGC_259_13,(7,1,4):C.UVGC_260_15,(7,1,5):C.UVGC_260_16,(5,1,4):C.UVGC_254_5,(5,1,5):C.UVGC_254_6,(1,1,4):C.UVGC_254_5,(1,1,5):C.UVGC_254_6,(11,1,4):C.UVGC_258_11,(11,1,5):C.UVGC_258_12,(10,1,4):C.UVGC_258_11,(10,1,5):C.UVGC_258_12,(9,1,4):C.UVGC_257_9,(9,1,5):C.UVGC_257_10,(2,2,4):C.UVGC_255_8,(2,2,5):C.UVGC_255_7,(0,2,4):C.UVGC_255_8,(0,2,5):C.UVGC_255_7,(4,2,4):C.UVGC_254_5,(4,2,5):C.UVGC_254_6,(3,2,4):C.UVGC_254_5,(3,2,5):C.UVGC_254_6,(8,2,0):C.UVGC_349_168,(8,2,2):C.UVGC_349_169,(8,2,3):C.UVGC_349_170,(8,2,4):C.UVGC_349_171,(8,2,5):C.UVGC_349_172,(8,2,6):C.UVGC_349_173,(8,2,7):C.UVGC_349_174,(8,2,8):C.UVGC_349_175,(6,2,1):C.UVGC_259_13,(6,2,4):C.UVGC_259_14,(6,2,5):C.UVGC_257_9,(7,2,0):C.UVGC_350_176,(7,2,2):C.UVGC_350_177,(7,2,3):C.UVGC_350_178,(7,2,4):C.UVGC_351_184,(7,2,5):C.UVGC_351_185,(7,2,6):C.UVGC_350_181,(7,2,7):C.UVGC_350_182,(7,2,8):C.UVGC_350_183,(5,2,4):C.UVGC_254_5,(5,2,5):C.UVGC_254_6,(1,2,4):C.UVGC_254_5,(1,2,5):C.UVGC_254_6,(11,2,4):C.UVGC_258_11,(11,2,5):C.UVGC_258_12,(10,2,4):C.UVGC_258_11,(10,2,5):C.UVGC_258_12,(9,2,4):C.UVGC_257_9,(9,2,5):C.UVGC_257_10})

V_91 = CTVertex(name = 'V_91',
                type = 'UV',
                particles = [ P.u__tilde__, P.d, P.G__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.u] ], [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.UVGC_372_235,(0,0,2):C.UVGC_372_236,(0,0,1):C.UVGC_372_237,(0,1,0):C.UVGC_373_238,(0,1,2):C.UVGC_373_239,(0,1,1):C.UVGC_373_240})

V_92 = CTVertex(name = 'V_92',
                type = 'UV',
                particles = [ P.c__tilde__, P.d, P.G__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.c, P.d, P.g] ], [ [P.c, P.g] ], [ [P.d, P.g] ] ],
                couplings = {(0,0,1):C.UVGC_308_73,(0,0,2):C.UVGC_308_74,(0,0,0):C.UVGC_308_75,(0,1,1):C.UVGC_307_70,(0,1,2):C.UVGC_307_71,(0,1,0):C.UVGC_307_72})

V_93 = CTVertex(name = 'V_93',
                type = 'UV',
                particles = [ P.u__tilde__, P.s, P.G__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.u] ], [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.UVGC_375_244,(0,0,2):C.UVGC_375_245,(0,0,1):C.UVGC_375_246,(0,1,0):C.UVGC_376_247,(0,1,2):C.UVGC_376_248,(0,1,1):C.UVGC_376_249})

V_94 = CTVertex(name = 'V_94',
                type = 'UV',
                particles = [ P.c__tilde__, P.s, P.G__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.s] ], [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.UVGC_324_101,(0,0,2):C.UVGC_324_102,(0,0,1):C.UVGC_324_103,(0,1,0):C.UVGC_323_98,(0,1,2):C.UVGC_323_99,(0,1,1):C.UVGC_323_100})

V_95 = CTVertex(name = 'V_95',
                type = 'UV',
                particles = [ P.t__tilde__, P.b, P.G__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS4 ],
                loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_339_126,(0,0,2):C.UVGC_339_127,(0,0,1):C.UVGC_339_128,(0,1,0):C.UVGC_340_129,(0,1,2):C.UVGC_340_130,(0,1,1):C.UVGC_340_131})

V_96 = CTVertex(name = 'V_96',
                type = 'UV',
                particles = [ P.d__tilde__, P.d, P.G0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_301_60})

V_97 = CTVertex(name = 'V_97',
                type = 'UV',
                particles = [ P.s__tilde__, P.s, P.G0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.UVGC_317_88})

V_98 = CTVertex(name = 'V_98',
                type = 'UV',
                particles = [ P.b__tilde__, P.b, P.G0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_279_34})

V_99 = CTVertex(name = 'V_99',
                type = 'UV',
                particles = [ P.d__tilde__, P.d, P.H3 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_303_64})

V_100 = CTVertex(name = 'V_100',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s, P.H3 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS2 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_319_92})

V_101 = CTVertex(name = 'V_101',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b, P.H3 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS2 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_280_35})

V_102 = CTVertex(name = 'V_102',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.d, P.H2 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS2 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_304_65})

V_103 = CTVertex(name = 'V_103',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s, P.H2 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS2 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_320_93})

V_104 = CTVertex(name = 'V_104',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b, P.H2 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS2 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_281_36})

V_105 = CTVertex(name = 'V_105',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.d, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS2 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_305_66})

V_106 = CTVertex(name = 'V_106',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS2 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_321_94})

V_107 = CTVertex(name = 'V_107',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS2 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_282_37})

V_108 = CTVertex(name = 'V_108',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.u, P.G__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.u] ], [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_366_223,(0,0,2):C.UVGC_366_224,(0,0,1):C.UVGC_366_225,(0,1,0):C.UVGC_363_216,(0,1,2):C.UVGC_363_217,(0,1,1):C.UVGC_363_218})

V_109 = CTVertex(name = 'V_109',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.u, P.G__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.u] ], [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_367_226,(0,0,2):C.UVGC_367_227,(0,0,1):C.UVGC_367_228,(0,1,0):C.UVGC_364_219,(0,1,2):C.UVGC_364_220,(0,1,1):C.UVGC_364_221})

V_110 = CTVertex(name = 'V_110',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.c, P.G__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.c, P.d, P.g] ], [ [P.c, P.g] ], [ [P.d, P.g] ] ],
                 couplings = {(0,0,1):C.UVGC_300_57,(0,0,2):C.UVGC_300_58,(0,0,0):C.UVGC_300_59,(0,1,1):C.UVGC_302_61,(0,1,2):C.UVGC_302_62,(0,1,0):C.UVGC_302_63})

V_111 = CTVertex(name = 'V_111',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.c, P.G__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.s] ], [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_316_85,(0,0,2):C.UVGC_316_86,(0,0,1):C.UVGC_316_87,(0,1,0):C.UVGC_318_89,(0,1,2):C.UVGC_318_90,(0,1,1):C.UVGC_318_91})

V_112 = CTVertex(name = 'V_112',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.t, P.G__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS3, L.FFS4 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_334_117,(0,0,2):C.UVGC_334_118,(0,0,1):C.UVGC_334_119,(0,1,0):C.UVGC_332_113,(0,1,2):C.UVGC_332_114,(0,1,1):C.UVGC_332_115})

V_113 = CTVertex(name = 'V_113',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u, P.G0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS1 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_365_222})

V_114 = CTVertex(name = 'V_114',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c, P.G0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS1 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_289_44})

V_115 = CTVertex(name = 'V_115',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.G0 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS1 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_333_116})

V_116 = CTVertex(name = 'V_116',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u, P.H3 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS2 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_368_229})

V_117 = CTVertex(name = 'V_117',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c, P.H3 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS2 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_290_45})

V_118 = CTVertex(name = 'V_118',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.H3 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS2 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_335_120})

V_119 = CTVertex(name = 'V_119',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u, P.H2 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS2 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_369_230})

V_120 = CTVertex(name = 'V_120',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c, P.H2 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS2 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_291_46})

V_121 = CTVertex(name = 'V_121',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.H2 ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS2 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_336_121})

V_122 = CTVertex(name = 'V_122',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS2 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_370_231})

V_123 = CTVertex(name = 'V_123',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS2 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_292_47})

V_124 = CTVertex(name = 'V_124',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.H ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFS2 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_337_122})

V_125 = CTVertex(name = 'V_125',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV4 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_263_19,(0,1,0):C.UVGC_356_205})

V_126 = CTVertex(name = 'V_126',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV4 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_263_19,(0,1,0):C.UVGC_284_39})

V_127 = CTVertex(name = 'V_127',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV4 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_263_19,(0,1,0):C.UVGC_326_105})

V_128 = CTVertex(name = 'V_128',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.d, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV4 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_261_17,(0,1,0):C.UVGC_294_49})

V_129 = CTVertex(name = 'V_129',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV4 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_261_17,(0,1,0):C.UVGC_310_77})

V_130 = CTVertex(name = 'V_130',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b, P.a ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV1, L.FFV4 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_261_17,(0,1,0):C.UVGC_274_21})

V_131 = CTVertex(name = 'V_131',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV4 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.u] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                 couplings = {(0,0,5):C.UVGC_262_18,(0,1,0):C.UVGC_275_22,(0,1,1):C.UVGC_275_23,(0,1,2):C.UVGC_275_24,(0,1,3):C.UVGC_275_25,(0,1,4):C.UVGC_275_26,(0,1,6):C.UVGC_275_27,(0,1,7):C.UVGC_275_28,(0,1,8):C.UVGC_275_29,(0,1,5):C.UVGC_357_206})

V_132 = CTVertex(name = 'V_132',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV4 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.c, P.g] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                 couplings = {(0,0,2):C.UVGC_262_18,(0,1,0):C.UVGC_275_22,(0,1,1):C.UVGC_275_23,(0,1,3):C.UVGC_275_24,(0,1,4):C.UVGC_275_25,(0,1,5):C.UVGC_275_26,(0,1,6):C.UVGC_275_27,(0,1,7):C.UVGC_275_28,(0,1,8):C.UVGC_275_29,(0,1,2):C.UVGC_285_40})

V_133 = CTVertex(name = 'V_133',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV4 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.t] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                 couplings = {(0,0,5):C.UVGC_262_18,(0,1,0):C.UVGC_275_22,(0,1,1):C.UVGC_275_23,(0,1,2):C.UVGC_275_24,(0,1,3):C.UVGC_275_25,(0,1,4):C.UVGC_275_26,(0,1,6):C.UVGC_275_27,(0,1,7):C.UVGC_275_28,(0,1,8):C.UVGC_275_29,(0,1,5):C.UVGC_327_106})

V_134 = CTVertex(name = 'V_134',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.d, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV4 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.d, P.g] ], [ [P.g] ], [ [P.ghG] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                 couplings = {(0,0,3):C.UVGC_262_18,(0,1,0):C.UVGC_275_22,(0,1,1):C.UVGC_275_23,(0,1,2):C.UVGC_275_24,(0,1,4):C.UVGC_275_25,(0,1,5):C.UVGC_275_26,(0,1,6):C.UVGC_275_27,(0,1,7):C.UVGC_275_28,(0,1,8):C.UVGC_275_29,(0,1,3):C.UVGC_295_50})

V_135 = CTVertex(name = 'V_135',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV4 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.s] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                 couplings = {(0,0,5):C.UVGC_262_18,(0,1,0):C.UVGC_275_22,(0,1,1):C.UVGC_275_23,(0,1,2):C.UVGC_275_24,(0,1,3):C.UVGC_275_25,(0,1,4):C.UVGC_275_26,(0,1,6):C.UVGC_275_27,(0,1,7):C.UVGC_275_28,(0,1,8):C.UVGC_275_29,(0,1,5):C.UVGC_311_78})

V_136 = CTVertex(name = 'V_136',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b, P.g ],
                 color = [ 'T(3,2,1)' ],
                 lorentz = [ L.FFV1, L.FFV4 ],
                 loop_particles = [ [ [P.b] ], [ [P.b, P.g] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                 couplings = {(0,0,1):C.UVGC_262_18,(0,1,0):C.UVGC_275_22,(0,1,2):C.UVGC_275_23,(0,1,3):C.UVGC_275_24,(0,1,4):C.UVGC_275_25,(0,1,5):C.UVGC_275_26,(0,1,6):C.UVGC_275_27,(0,1,7):C.UVGC_275_28,(0,1,8):C.UVGC_275_29,(0,1,1):C.UVGC_275_30})

V_137 = CTVertex(name = 'V_137',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.u, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.u] ], [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_359_208,(0,0,2):C.UVGC_359_209,(0,0,1):C.UVGC_359_210})

V_138 = CTVertex(name = 'V_138',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.u, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.u] ], [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_360_211,(0,0,2):C.UVGC_360_212,(0,0,1):C.UVGC_360_213})

V_139 = CTVertex(name = 'V_139',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.c, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.d, P.g] ], [ [P.c, P.g] ], [ [P.d, P.g] ] ],
                 couplings = {(0,0,1):C.UVGC_297_52,(0,0,2):C.UVGC_297_53,(0,0,0):C.UVGC_297_54})

V_140 = CTVertex(name = 'V_140',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.c, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.s] ], [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_313_80,(0,0,2):C.UVGC_313_81,(0,0,1):C.UVGC_313_82})

V_141 = CTVertex(name = 'V_141',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.t, P.W__minus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_329_108,(0,0,2):C.UVGC_329_109,(0,0,1):C.UVGC_329_110})

V_142 = CTVertex(name = 'V_142',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.d, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.g, P.u] ], [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_371_232,(0,0,2):C.UVGC_371_233,(0,0,1):C.UVGC_371_234})

V_143 = CTVertex(name = 'V_143',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.d, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.d, P.g] ], [ [P.c, P.g] ], [ [P.d, P.g] ] ],
                 couplings = {(0,0,1):C.UVGC_306_67,(0,0,2):C.UVGC_306_68,(0,0,0):C.UVGC_306_69})

V_144 = CTVertex(name = 'V_144',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.s, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.g, P.s] ], [ [P.g, P.s, P.u] ], [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_374_241,(0,0,2):C.UVGC_374_242,(0,0,1):C.UVGC_374_243})

V_145 = CTVertex(name = 'V_145',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.s, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.g, P.s] ], [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_322_95,(0,0,2):C.UVGC_322_96,(0,0,1):C.UVGC_322_97})

V_146 = CTVertex(name = 'V_146',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.b, P.W__plus__ ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2 ],
                 loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_338_123,(0,0,2):C.UVGC_338_124,(0,0,1):C.UVGC_338_125})

V_147 = CTVertex(name = 'V_147',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_361_214,(0,1,0):C.UVGC_362_215})

V_148 = CTVertex(name = 'V_148',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_287_42,(0,1,0):C.UVGC_288_43})

V_149 = CTVertex(name = 'V_149',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_330_111,(0,1,0):C.UVGC_331_112})

V_150 = CTVertex(name = 'V_150',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.d, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_298_55,(0,1,0):C.UVGC_299_56})

V_151 = CTVertex(name = 'V_151',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_314_83,(0,1,0):C.UVGC_315_84})

V_152 = CTVertex(name = 'V_152',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b, P.Z ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FFV2, L.FFV3 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_277_32,(0,1,0):C.UVGC_278_33})

V_153 = CTVertex(name = 'V_153',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF2, L.FF3, L.FF4 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_358_207,(0,2,0):C.UVGC_358_207,(0,1,0):C.UVGC_355_204,(0,3,0):C.UVGC_355_204})

V_154 = CTVertex(name = 'V_154',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF2, L.FF3, L.FF4 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_286_41,(0,2,0):C.UVGC_286_41,(0,1,0):C.UVGC_283_38,(0,3,0):C.UVGC_283_38})

V_155 = CTVertex(name = 'V_155',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF2, L.FF3, L.FF4 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_328_107,(0,2,0):C.UVGC_328_107,(0,1,0):C.UVGC_325_104,(0,3,0):C.UVGC_325_104})

V_156 = CTVertex(name = 'V_156',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.d ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF2, L.FF3, L.FF4 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_296_51,(0,2,0):C.UVGC_296_51,(0,1,0):C.UVGC_293_48,(0,3,0):C.UVGC_293_48})

V_157 = CTVertex(name = 'V_157',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF2, L.FF3, L.FF4 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_312_79,(0,2,0):C.UVGC_312_79,(0,1,0):C.UVGC_309_76,(0,3,0):C.UVGC_309_76})

V_158 = CTVertex(name = 'V_158',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF2, L.FF3, L.FF4 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_276_31,(0,2,0):C.UVGC_276_31,(0,1,0):C.UVGC_273_20,(0,3,0):C.UVGC_273_20})

V_159 = CTVertex(name = 'V_159',
                 type = 'UV',
                 particles = [ P.g, P.g ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VV1, L.VV3 ],
                 loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g] ], [ [P.ghG] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_342_138,(0,0,1):C.UVGC_342_139,(0,0,2):C.UVGC_342_140,(0,0,3):C.UVGC_342_141,(0,0,4):C.UVGC_342_142,(0,0,5):C.UVGC_342_143,(0,0,6):C.UVGC_342_144,(0,0,7):C.UVGC_342_145,(0,1,0):C.UVGC_341_132,(0,1,1):C.UVGC_341_133,(0,1,2):C.UVGC_341_134,(0,1,5):C.UVGC_341_135,(0,1,6):C.UVGC_341_136,(0,1,7):C.UVGC_341_137})

