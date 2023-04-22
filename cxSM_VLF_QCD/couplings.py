# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 12.3.1 for Microsoft Windows (64-bit) (June 24, 2021)
# Date: Wed 19 Oct 2022 16:38:21


from object_library import all_couplings, Coupling

from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot



GC_1 = Coupling(name = 'GC_1',
                value = '-0.3333333333333333*(ee*complex(0,1))',
                order = {'QED':1})

GC_10 = Coupling(name = 'GC_10',
                 value = 'G',
                 order = {'QCD':1})

GC_100 = Coupling(name = 'GC_100',
                  value = '(CKM2x1*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_101 = Coupling(name = 'GC_101',
                  value = '(CKM2x2*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_102 = Coupling(name = 'GC_102',
                  value = '(CKM2x3*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_103 = Coupling(name = 'GC_103',
                  value = '(CKM3x1*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_104 = Coupling(name = 'GC_104',
                  value = '(CKM3x2*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_105 = Coupling(name = 'GC_105',
                  value = '(CKM3x3*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_106 = Coupling(name = 'GC_106',
                  value = '-((cw*ee*complex(0,1))/sw)',
                  order = {'QED':1})

GC_107 = Coupling(name = 'GC_107',
                  value = '(cw*ee*complex(0,1))/sw',
                  order = {'QED':1})

GC_108 = Coupling(name = 'GC_108',
                  value = '-0.5*(ee**2*complex(0,1))/sw',
                  order = {'QED':2})

GC_109 = Coupling(name = 'GC_109',
                  value = '(-2*cw*ee**2*complex(0,1))/sw',
                  order = {'QED':2})

GC_11 = Coupling(name = 'GC_11',
                 value = '-(complex(0,1)*G**2)',
                 order = {'QCD':2})

GC_110 = Coupling(name = 'GC_110',
                  value = '-0.5*(ee*R11)/sw',
                  order = {'QED':1})

GC_111 = Coupling(name = 'GC_111',
                  value = '-0.5*(ee**2*R11)/sw',
                  order = {'QED':2})

GC_112 = Coupling(name = 'GC_112',
                  value = '(ee**2*R11)/(2.*sw)',
                  order = {'QED':2})

GC_113 = Coupling(name = 'GC_113',
                  value = '-0.5*(ee*R12)/sw',
                  order = {'QED':1})

GC_114 = Coupling(name = 'GC_114',
                  value = '-0.5*(ee**2*R12)/sw',
                  order = {'QED':2})

GC_115 = Coupling(name = 'GC_115',
                  value = '(ee**2*R12)/(2.*sw)',
                  order = {'QED':2})

GC_116 = Coupling(name = 'GC_116',
                  value = '-0.5*(ee*R13)/sw',
                  order = {'QED':1})

GC_117 = Coupling(name = 'GC_117',
                  value = '-0.5*(ee**2*R13)/sw',
                  order = {'QED':2})

GC_118 = Coupling(name = 'GC_118',
                  value = '(ee**2*R13)/(2.*sw)',
                  order = {'QED':2})

GC_119 = Coupling(name = 'GC_119',
                  value = '(ee*complex(0,1)*sw)/(3.*cw)',
                  order = {'QED':1})

GC_12 = Coupling(name = 'GC_12',
                 value = 'complex(0,1)*G**2',
                 order = {'QCD':2})

GC_120 = Coupling(name = 'GC_120',
                  value = '(-2*ee*complex(0,1)*sw)/(3.*cw)',
                  order = {'QED':1})

GC_121 = Coupling(name = 'GC_121',
                  value = '(ee*complex(0,1)*sw)/cw',
                  order = {'QED':1})

GC_122 = Coupling(name = 'GC_122',
                  value = '-0.5*(cw*ee*complex(0,1))/sw - (ee*complex(0,1)*sw)/(6.*cw)',
                  order = {'QED':1})

GC_123 = Coupling(name = 'GC_123',
                  value = '(cw*ee*complex(0,1))/(2.*sw) - (ee*complex(0,1)*sw)/(6.*cw)',
                  order = {'QED':1})

GC_124 = Coupling(name = 'GC_124',
                  value = '-0.5*(cw*ee*complex(0,1))/sw + (ee*complex(0,1)*sw)/(2.*cw)',
                  order = {'QED':1})

GC_125 = Coupling(name = 'GC_125',
                  value = '(cw*ee*complex(0,1))/(2.*sw) + (ee*complex(0,1)*sw)/(2.*cw)',
                  order = {'QED':1})

GC_126 = Coupling(name = 'GC_126',
                  value = '(cw*ee**2*complex(0,1))/sw - (ee**2*complex(0,1)*sw)/cw',
                  order = {'QED':2})

GC_127 = Coupling(name = 'GC_127',
                  value = '-0.5*(cw*ee*R11)/sw - (ee*R11*sw)/(2.*cw)',
                  order = {'QED':1})

GC_128 = Coupling(name = 'GC_128',
                  value = '-0.5*(cw*ee*R12)/sw - (ee*R12*sw)/(2.*cw)',
                  order = {'QED':1})

GC_129 = Coupling(name = 'GC_129',
                  value = '-0.5*(cw*ee*R13)/sw - (ee*R13*sw)/(2.*cw)',
                  order = {'QED':1})

GC_13 = Coupling(name = 'GC_13',
                 value = 'I1a11',
                 order = {'QED':1})

GC_130 = Coupling(name = 'GC_130',
                  value = '-(ee**2*complex(0,1)) + (cw**2*ee**2*complex(0,1))/(2.*sw**2) + (ee**2*complex(0,1)*sw**2)/(2.*cw**2)',
                  order = {'QED':2})

GC_131 = Coupling(name = 'GC_131',
                  value = 'ee**2*complex(0,1) + (cw**2*ee**2*complex(0,1))/(2.*sw**2) + (ee**2*complex(0,1)*sw**2)/(2.*cw**2)',
                  order = {'QED':2})

GC_132 = Coupling(name = 'GC_132',
                  value = 'ee**2*complex(0,1)*R11**2 + (cw**2*ee**2*complex(0,1)*R11**2)/(2.*sw**2) + (ee**2*complex(0,1)*R11**2*sw**2)/(2.*cw**2)',
                  order = {'QED':2})

GC_133 = Coupling(name = 'GC_133',
                  value = 'ee**2*complex(0,1)*R11*R12 + (cw**2*ee**2*complex(0,1)*R11*R12)/(2.*sw**2) + (ee**2*complex(0,1)*R11*R12*sw**2)/(2.*cw**2)',
                  order = {'QED':2})

GC_134 = Coupling(name = 'GC_134',
                  value = 'ee**2*complex(0,1)*R12**2 + (cw**2*ee**2*complex(0,1)*R12**2)/(2.*sw**2) + (ee**2*complex(0,1)*R12**2*sw**2)/(2.*cw**2)',
                  order = {'QED':2})

GC_135 = Coupling(name = 'GC_135',
                  value = 'ee**2*complex(0,1)*R11*R13 + (cw**2*ee**2*complex(0,1)*R11*R13)/(2.*sw**2) + (ee**2*complex(0,1)*R11*R13*sw**2)/(2.*cw**2)',
                  order = {'QED':2})

GC_136 = Coupling(name = 'GC_136',
                  value = 'ee**2*complex(0,1)*R12*R13 + (cw**2*ee**2*complex(0,1)*R12*R13)/(2.*sw**2) + (ee**2*complex(0,1)*R12*R13*sw**2)/(2.*cw**2)',
                  order = {'QED':2})

GC_137 = Coupling(name = 'GC_137',
                  value = 'ee**2*complex(0,1)*R13**2 + (cw**2*ee**2*complex(0,1)*R13**2)/(2.*sw**2) + (ee**2*complex(0,1)*R13**2*sw**2)/(2.*cw**2)',
                  order = {'QED':2})

GC_138 = Coupling(name = 'GC_138',
                  value = '-0.5*(ee**2*vev)/cw',
                  order = {'QED':1})

GC_139 = Coupling(name = 'GC_139',
                  value = '(ee**2*vev)/(2.*cw)',
                  order = {'QED':1})

GC_14 = Coupling(name = 'GC_14',
                 value = 'I1a12',
                 order = {'QED':1})

GC_140 = Coupling(name = 'GC_140',
                  value = '-0.25*(ee**2*vev)/sw**2',
                  order = {'QED':1})

GC_141 = Coupling(name = 'GC_141',
                  value = '(ee**2*vev)/(4.*sw**2)',
                  order = {'QED':1})

GC_142 = Coupling(name = 'GC_142',
                  value = '-0.25*(ee**2*complex(0,1)*R11*vev)/sw**2',
                  order = {'QED':1})

GC_143 = Coupling(name = 'GC_143',
                  value = '(ee**2*complex(0,1)*R11*vev)/(2.*sw**2)',
                  order = {'QED':1})

GC_144 = Coupling(name = 'GC_144',
                  value = '-0.25*(ee**2*complex(0,1)*R12*vev)/sw**2',
                  order = {'QED':1})

GC_145 = Coupling(name = 'GC_145',
                  value = '(ee**2*complex(0,1)*R12*vev)/(2.*sw**2)',
                  order = {'QED':1})

GC_146 = Coupling(name = 'GC_146',
                  value = '-0.25*(ee**2*complex(0,1)*R13*vev)/sw**2',
                  order = {'QED':1})

GC_147 = Coupling(name = 'GC_147',
                  value = '(ee**2*complex(0,1)*R13*vev)/(2.*sw**2)',
                  order = {'QED':1})

GC_148 = Coupling(name = 'GC_148',
                  value = '-0.5*(ee**2*vev)/sw',
                  order = {'QED':1})

GC_149 = Coupling(name = 'GC_149',
                  value = '(ee**2*vev)/(2.*sw)',
                  order = {'QED':1})

GC_15 = Coupling(name = 'GC_15',
                 value = 'I1a13',
                 order = {'QED':1})

GC_150 = Coupling(name = 'GC_150',
                  value = '-0.25*(ee**2*vev)/cw - (cw*ee**2*vev)/(4.*sw**2)',
                  order = {'QED':1})

GC_151 = Coupling(name = 'GC_151',
                  value = '(ee**2*vev)/(4.*cw) - (cw*ee**2*vev)/(4.*sw**2)',
                  order = {'QED':1})

GC_152 = Coupling(name = 'GC_152',
                  value = '-0.25*(ee**2*vev)/cw + (cw*ee**2*vev)/(4.*sw**2)',
                  order = {'QED':1})

GC_153 = Coupling(name = 'GC_153',
                  value = '(ee**2*vev)/(4.*cw) + (cw*ee**2*vev)/(4.*sw**2)',
                  order = {'QED':1})

GC_154 = Coupling(name = 'GC_154',
                  value = '-0.5*(ee**2*complex(0,1)*R11*vev) - (cw**2*ee**2*complex(0,1)*R11*vev)/(4.*sw**2) - (ee**2*complex(0,1)*R11*sw**2*vev)/(4.*cw**2)',
                  order = {'QED':1})

GC_155 = Coupling(name = 'GC_155',
                  value = 'ee**2*complex(0,1)*R11*vev + (cw**2*ee**2*complex(0,1)*R11*vev)/(2.*sw**2) + (ee**2*complex(0,1)*R11*sw**2*vev)/(2.*cw**2)',
                  order = {'QED':1})

GC_156 = Coupling(name = 'GC_156',
                  value = '-0.5*(ee**2*complex(0,1)*R12*vev) - (cw**2*ee**2*complex(0,1)*R12*vev)/(4.*sw**2) - (ee**2*complex(0,1)*R12*sw**2*vev)/(4.*cw**2)',
                  order = {'QED':1})

GC_157 = Coupling(name = 'GC_157',
                  value = 'ee**2*complex(0,1)*R12*vev + (cw**2*ee**2*complex(0,1)*R12*vev)/(2.*sw**2) + (ee**2*complex(0,1)*R12*sw**2*vev)/(2.*cw**2)',
                  order = {'QED':1})

GC_158 = Coupling(name = 'GC_158',
                  value = '-0.5*(ee**2*complex(0,1)*R13*vev) - (cw**2*ee**2*complex(0,1)*R13*vev)/(4.*sw**2) - (ee**2*complex(0,1)*R13*sw**2*vev)/(4.*cw**2)',
                  order = {'QED':1})

GC_159 = Coupling(name = 'GC_159',
                  value = 'ee**2*complex(0,1)*R13*vev + (cw**2*ee**2*complex(0,1)*R13*vev)/(2.*sw**2) + (ee**2*complex(0,1)*R13*sw**2*vev)/(2.*cw**2)',
                  order = {'QED':1})

GC_16 = Coupling(name = 'GC_16',
                 value = 'I1a21',
                 order = {'QED':1})

GC_160 = Coupling(name = 'GC_160',
                  value = '-2*complex(0,1)*lam*R11*vev - (delta2*complex(0,1)*R21*vs)/2. + (complex(0,1)*Idelta3*R31*vs)/2. - (complex(0,1)*R21*Rdelta3*vs)/2. + (complex(0,1)*Idelta1*R31)/(2.*cmath.sqrt(2)) - (complex(0,1)*R21*Rdelta1)/(2.*cmath.sqrt(2))',
                  order = {'QED':1})

GC_161 = Coupling(name = 'GC_161',
                  value = '-6*complex(0,1)*lam*R11**3*vev - (3*delta2*complex(0,1)*R11*R21**2*vev)/2. + 3*complex(0,1)*Idelta3*R11*R21*R31*vev - (3*delta2*complex(0,1)*R11*R31**2*vev)/2. - (3*complex(0,1)*R11*R21**2*Rdelta3*vev)/2. + (3*complex(0,1)*R11*R31**2*Rdelta3*vev)/2. - (3*delta2*complex(0,1)*R11**2*R21*vs)/2. - (3*d2*complex(0,1)*R21**3*vs)/2. + (3*complex(0,1)*Idelta3*R11**2*R31*vs)/2. + (9*complex(0,1)*Id1*R21**2*R31*vs)/2. - (3*d2*complex(0,1)*R21*R31**2*vs)/2. - (3*complex(0,1)*Id1*R31**3*vs)/2. - (3*complex(0,1)*R21**3*Rd1*vs)/2. + (9*complex(0,1)*R21*R31**2*Rd1*vs)/2. - (3*complex(0,1)*R21**3*Rd3*vs)/2. + (9*R21**2*R31*Rd3*vs)/4. + (3*R31**3*Rd3*vs)/4. - (3*complex(0,1)*R11**2*R21*Rdelta3*vs)/2. + (3*complex(0,1)*Idelta1*R11**2*R31)/(2.*cmath.sqrt(2)) + (3*complex(0,1)*Ic1*R21**2*R31)/cmath.sqrt(2) + (complex(0,1)*Ic2*R21**2*R31)/cmath.sqrt(2) - (complex(0,1)*Ic1*R31**3)/cmath.sqrt(2) + (complex(0,1)*Ic2*R31**3)/cmath.sqrt(2) - (complex(0,1)*R21**3*Rc1)/cmath.sqrt(2) + (3*complex(0,1)*R21*R31**2*Rc1)/cmath.sqrt(2) - (complex(0,1)*R21**3*Rc2)/cmath.sqrt(2) - (complex(0,1)*R21*R31**2*Rc2)/cmath.sqrt(2) - (3*complex(0,1)*R11**2*R21*Rdelta1)/(2.*cmath.sqrt(2))',
                  order = {'QED':1})

GC_162 = Coupling(name = 'GC_162',
                  value = '-2*complex(0,1)*lam*R12*vev - (delta2*complex(0,1)*R22*vs)/2. + (complex(0,1)*Idelta3*R32*vs)/2. - (complex(0,1)*R22*Rdelta3*vs)/2. + (complex(0,1)*Idelta1*R32)/(2.*cmath.sqrt(2)) - (complex(0,1)*R22*Rdelta1)/(2.*cmath.sqrt(2))',
                  order = {'QED':1})

GC_163 = Coupling(name = 'GC_163',
                  value = '-6*complex(0,1)*lam*R11**2*R12*vev - (delta2*complex(0,1)*R12*R21**2*vev)/2. - delta2*complex(0,1)*R11*R21*R22*vev + complex(0,1)*Idelta3*R12*R21*R31*vev + complex(0,1)*Idelta3*R11*R22*R31*vev - (delta2*complex(0,1)*R12*R31**2*vev)/2. + complex(0,1)*Idelta3*R11*R21*R32*vev - delta2*complex(0,1)*R11*R31*R32*vev - (complex(0,1)*R12*R21**2*Rdelta3*vev)/2. - complex(0,1)*R11*R21*R22*Rdelta3*vev + (complex(0,1)*R12*R31**2*Rdelta3*vev)/2. + complex(0,1)*R11*R31*R32*Rdelta3*vev - delta2*complex(0,1)*R11*R12*R21*vs - (delta2*complex(0,1)*R11**2*R22*vs)/2. - (3*d2*complex(0,1)*R21**2*R22*vs)/2. + complex(0,1)*Idelta3*R11*R12*R31*vs + 3*complex(0,1)*Id1*R21*R22*R31*vs - (d2*complex(0,1)*R22*R31**2*vs)/2. + (complex(0,1)*Idelta3*R11**2*R32*vs)/2. + (3*complex(0,1)*Id1*R21**2*R32*vs)/2. - d2*complex(0,1)*R21*R31*R32*vs - (3*complex(0,1)*Id1*R31**2*R32*vs)/2. - (3*complex(0,1)*R21**2*R22*Rd1*vs)/2. + (3*complex(0,1)*R22*R31**2*Rd1*vs)/2. + 3*complex(0,1)*R21*R31*R32*Rd1*vs - (3*complex(0,1)*R21**2*R22*Rd3*vs)/2. + (3*R21*R22*R31*Rd3*vs)/2. + (3*R21**2*R32*Rd3*vs)/4. + (3*R31**2*R32*Rd3*vs)/4. - complex(0,1)*R11*R12*R21*Rdelta3*vs - (complex(0,1)*R11**2*R22*Rdelta3*vs)/2. + (complex(0,1)*Idelta1*R11*R12*R31)/cmath.sqrt(2) + (complex(0,1)*Idelta1*R11**2*R32)/(2.*cmath.sqrt(2)) + (complex(0,1)*Ic1*R21**2*R32)/cmath.sqrt(2) + (complex(0,1)*Ic2*R21**2*R32)/(3.*cmath.sqrt(2)) - (complex(0,1)*Ic1*R31**2*R32)/cmath.sqrt(2) + (complex(0,1)*Ic2*R31**2*R32)/cmath.sqrt(2) - (complex(0,1)*R21**2*R22*Rc1)/cmath.sqrt(2) + (complex(0,1)*R22*R31**2*Rc1)/cmath.sqrt(2) - (complex(0,1)*R21**2*R22*Rc2)/cmath.sqrt(2) - (complex(0,1)*R22*R31**2*Rc2)/(3.*cmath.sqrt(2)) - (complex(0,1)*R11*R12*R21*Rdelta1)/cmath.sqrt(2) - (complex(0,1)*R11**2*R22*Rdelta1)/(2.*cmath.sqrt(2)) + complex(0,1)*Ic1*R21*R22*R31*cmath.sqrt(2) + (complex(0,1)*Ic2*R21*R22*R31*cmath.sqrt(2))/3. + complex(0,1)*R21*R31*R32*Rc1*cmath.sqrt(2) - (complex(0,1)*R21*R31*R32*Rc2*cmath.sqrt(2))/3.',
                  order = {'QED':1})

GC_164 = Coupling(name = 'GC_164',
                  value = '-6*complex(0,1)*lam*R11*R12**2*vev - delta2*complex(0,1)*R12*R21*R22*vev - (delta2*complex(0,1)*R11*R22**2*vev)/2. + complex(0,1)*Idelta3*R12*R22*R31*vev + complex(0,1)*Idelta3*R12*R21*R32*vev + complex(0,1)*Idelta3*R11*R22*R32*vev - delta2*complex(0,1)*R12*R31*R32*vev - (delta2*complex(0,1)*R11*R32**2*vev)/2. - complex(0,1)*R12*R21*R22*Rdelta3*vev - (complex(0,1)*R11*R22**2*Rdelta3*vev)/2. + complex(0,1)*R12*R31*R32*Rdelta3*vev + (complex(0,1)*R11*R32**2*Rdelta3*vev)/2. - (delta2*complex(0,1)*R12**2*R21*vs)/2. - delta2*complex(0,1)*R11*R12*R22*vs - (3*d2*complex(0,1)*R21*R22**2*vs)/2. + (complex(0,1)*Idelta3*R12**2*R31*vs)/2. + (3*complex(0,1)*Id1*R22**2*R31*vs)/2. + complex(0,1)*Idelta3*R11*R12*R32*vs + 3*complex(0,1)*Id1*R21*R22*R32*vs - d2*complex(0,1)*R22*R31*R32*vs - (d2*complex(0,1)*R21*R32**2*vs)/2. - (3*complex(0,1)*Id1*R31*R32**2*vs)/2. - (3*complex(0,1)*R21*R22**2*Rd1*vs)/2. + 3*complex(0,1)*R22*R31*R32*Rd1*vs + (3*complex(0,1)*R21*R32**2*Rd1*vs)/2. - (3*complex(0,1)*R21*R22**2*Rd3*vs)/2. + (3*R22**2*R31*Rd3*vs)/4. + (3*R21*R22*R32*Rd3*vs)/2. + (3*R31*R32**2*Rd3*vs)/4. - (complex(0,1)*R12**2*R21*Rdelta3*vs)/2. - complex(0,1)*R11*R12*R22*Rdelta3*vs + (complex(0,1)*Idelta1*R12**2*R31)/(2.*cmath.sqrt(2)) + (complex(0,1)*Ic1*R22**2*R31)/cmath.sqrt(2) + (complex(0,1)*Ic2*R22**2*R31)/(3.*cmath.sqrt(2)) + (complex(0,1)*Idelta1*R11*R12*R32)/cmath.sqrt(2) - (complex(0,1)*Ic1*R31*R32**2)/cmath.sqrt(2) + (complex(0,1)*Ic2*R31*R32**2)/cmath.sqrt(2) - (complex(0,1)*R21*R22**2*Rc1)/cmath.sqrt(2) + (complex(0,1)*R21*R32**2*Rc1)/cmath.sqrt(2) - (complex(0,1)*R21*R22**2*Rc2)/cmath.sqrt(2) - (complex(0,1)*R21*R32**2*Rc2)/(3.*cmath.sqrt(2)) - (complex(0,1)*R12**2*R21*Rdelta1)/(2.*cmath.sqrt(2)) - (complex(0,1)*R11*R12*R22*Rdelta1)/cmath.sqrt(2) + complex(0,1)*Ic1*R21*R22*R32*cmath.sqrt(2) + (complex(0,1)*Ic2*R21*R22*R32*cmath.sqrt(2))/3. + complex(0,1)*R22*R31*R32*Rc1*cmath.sqrt(2) - (complex(0,1)*R22*R31*R32*Rc2*cmath.sqrt(2))/3.',
                  order = {'QED':1})

GC_165 = Coupling(name = 'GC_165',
                  value = '-6*complex(0,1)*lam*R12**3*vev - (3*delta2*complex(0,1)*R12*R22**2*vev)/2. + 3*complex(0,1)*Idelta3*R12*R22*R32*vev - (3*delta2*complex(0,1)*R12*R32**2*vev)/2. - (3*complex(0,1)*R12*R22**2*Rdelta3*vev)/2. + (3*complex(0,1)*R12*R32**2*Rdelta3*vev)/2. - (3*delta2*complex(0,1)*R12**2*R22*vs)/2. - (3*d2*complex(0,1)*R22**3*vs)/2. + (3*complex(0,1)*Idelta3*R12**2*R32*vs)/2. + (9*complex(0,1)*Id1*R22**2*R32*vs)/2. - (3*d2*complex(0,1)*R22*R32**2*vs)/2. - (3*complex(0,1)*Id1*R32**3*vs)/2. - (3*complex(0,1)*R22**3*Rd1*vs)/2. + (9*complex(0,1)*R22*R32**2*Rd1*vs)/2. - (3*complex(0,1)*R22**3*Rd3*vs)/2. + (9*R22**2*R32*Rd3*vs)/4. + (3*R32**3*Rd3*vs)/4. - (3*complex(0,1)*R12**2*R22*Rdelta3*vs)/2. + (3*complex(0,1)*Idelta1*R12**2*R32)/(2.*cmath.sqrt(2)) + (3*complex(0,1)*Ic1*R22**2*R32)/cmath.sqrt(2) + (complex(0,1)*Ic2*R22**2*R32)/cmath.sqrt(2) - (complex(0,1)*Ic1*R32**3)/cmath.sqrt(2) + (complex(0,1)*Ic2*R32**3)/cmath.sqrt(2) - (complex(0,1)*R22**3*Rc1)/cmath.sqrt(2) + (3*complex(0,1)*R22*R32**2*Rc1)/cmath.sqrt(2) - (complex(0,1)*R22**3*Rc2)/cmath.sqrt(2) - (complex(0,1)*R22*R32**2*Rc2)/cmath.sqrt(2) - (3*complex(0,1)*R12**2*R22*Rdelta1)/(2.*cmath.sqrt(2))',
                  order = {'QED':1})

GC_166 = Coupling(name = 'GC_166',
                  value = '-2*complex(0,1)*lam*R13*vev - (delta2*complex(0,1)*R23*vs)/2. + (complex(0,1)*Idelta3*R33*vs)/2. - (complex(0,1)*R23*Rdelta3*vs)/2. + (complex(0,1)*Idelta1*R33)/(2.*cmath.sqrt(2)) - (complex(0,1)*R23*Rdelta1)/(2.*cmath.sqrt(2))',
                  order = {'QED':1})

GC_167 = Coupling(name = 'GC_167',
                  value = '-6*complex(0,1)*lam*R11**2*R13*vev - (delta2*complex(0,1)*R13*R21**2*vev)/2. - delta2*complex(0,1)*R11*R21*R23*vev + complex(0,1)*Idelta3*R13*R21*R31*vev + complex(0,1)*Idelta3*R11*R23*R31*vev - (delta2*complex(0,1)*R13*R31**2*vev)/2. + complex(0,1)*Idelta3*R11*R21*R33*vev - delta2*complex(0,1)*R11*R31*R33*vev - (complex(0,1)*R13*R21**2*Rdelta3*vev)/2. - complex(0,1)*R11*R21*R23*Rdelta3*vev + (complex(0,1)*R13*R31**2*Rdelta3*vev)/2. + complex(0,1)*R11*R31*R33*Rdelta3*vev - delta2*complex(0,1)*R11*R13*R21*vs - (delta2*complex(0,1)*R11**2*R23*vs)/2. - (3*d2*complex(0,1)*R21**2*R23*vs)/2. + complex(0,1)*Idelta3*R11*R13*R31*vs + 3*complex(0,1)*Id1*R21*R23*R31*vs - (d2*complex(0,1)*R23*R31**2*vs)/2. + (complex(0,1)*Idelta3*R11**2*R33*vs)/2. + (3*complex(0,1)*Id1*R21**2*R33*vs)/2. - d2*complex(0,1)*R21*R31*R33*vs - (3*complex(0,1)*Id1*R31**2*R33*vs)/2. - (3*complex(0,1)*R21**2*R23*Rd1*vs)/2. + (3*complex(0,1)*R23*R31**2*Rd1*vs)/2. + 3*complex(0,1)*R21*R31*R33*Rd1*vs - (3*complex(0,1)*R21**2*R23*Rd3*vs)/2. + (3*R21*R23*R31*Rd3*vs)/2. + (3*R21**2*R33*Rd3*vs)/4. + (3*R31**2*R33*Rd3*vs)/4. - complex(0,1)*R11*R13*R21*Rdelta3*vs - (complex(0,1)*R11**2*R23*Rdelta3*vs)/2. + (complex(0,1)*Idelta1*R11*R13*R31)/cmath.sqrt(2) + (complex(0,1)*Idelta1*R11**2*R33)/(2.*cmath.sqrt(2)) + (complex(0,1)*Ic1*R21**2*R33)/cmath.sqrt(2) + (complex(0,1)*Ic2*R21**2*R33)/(3.*cmath.sqrt(2)) - (complex(0,1)*Ic1*R31**2*R33)/cmath.sqrt(2) + (complex(0,1)*Ic2*R31**2*R33)/cmath.sqrt(2) - (complex(0,1)*R21**2*R23*Rc1)/cmath.sqrt(2) + (complex(0,1)*R23*R31**2*Rc1)/cmath.sqrt(2) - (complex(0,1)*R21**2*R23*Rc2)/cmath.sqrt(2) - (complex(0,1)*R23*R31**2*Rc2)/(3.*cmath.sqrt(2)) - (complex(0,1)*R11*R13*R21*Rdelta1)/cmath.sqrt(2) - (complex(0,1)*R11**2*R23*Rdelta1)/(2.*cmath.sqrt(2)) + complex(0,1)*Ic1*R21*R23*R31*cmath.sqrt(2) + (complex(0,1)*Ic2*R21*R23*R31*cmath.sqrt(2))/3. + complex(0,1)*R21*R31*R33*Rc1*cmath.sqrt(2) - (complex(0,1)*R21*R31*R33*Rc2*cmath.sqrt(2))/3.',
                  order = {'QED':1})

GC_168 = Coupling(name = 'GC_168',
                  value = '-6*complex(0,1)*lam*R11*R12*R13*vev - (delta2*complex(0,1)*R13*R21*R22*vev)/2. - (delta2*complex(0,1)*R12*R21*R23*vev)/2. - (delta2*complex(0,1)*R11*R22*R23*vev)/2. + (complex(0,1)*Idelta3*R13*R22*R31*vev)/2. + (complex(0,1)*Idelta3*R12*R23*R31*vev)/2. + (complex(0,1)*Idelta3*R13*R21*R32*vev)/2. + (complex(0,1)*Idelta3*R11*R23*R32*vev)/2. - (delta2*complex(0,1)*R13*R31*R32*vev)/2. + (complex(0,1)*Idelta3*R12*R21*R33*vev)/2. + (complex(0,1)*Idelta3*R11*R22*R33*vev)/2. - (delta2*complex(0,1)*R12*R31*R33*vev)/2. - (delta2*complex(0,1)*R11*R32*R33*vev)/2. - (complex(0,1)*R13*R21*R22*Rdelta3*vev)/2. - (complex(0,1)*R12*R21*R23*Rdelta3*vev)/2. - (complex(0,1)*R11*R22*R23*Rdelta3*vev)/2. + (complex(0,1)*R13*R31*R32*Rdelta3*vev)/2. + (complex(0,1)*R12*R31*R33*Rdelta3*vev)/2. + (complex(0,1)*R11*R32*R33*Rdelta3*vev)/2. - (delta2*complex(0,1)*R12*R13*R21*vs)/2. - (delta2*complex(0,1)*R11*R13*R22*vs)/2. - (delta2*complex(0,1)*R11*R12*R23*vs)/2. - (3*d2*complex(0,1)*R21*R22*R23*vs)/2. + (complex(0,1)*Idelta3*R12*R13*R31*vs)/2. + (3*complex(0,1)*Id1*R22*R23*R31*vs)/2. + (complex(0,1)*Idelta3*R11*R13*R32*vs)/2. + (3*complex(0,1)*Id1*R21*R23*R32*vs)/2. - (d2*complex(0,1)*R23*R31*R32*vs)/2. + (complex(0,1)*Idelta3*R11*R12*R33*vs)/2. + (3*complex(0,1)*Id1*R21*R22*R33*vs)/2. - (d2*complex(0,1)*R22*R31*R33*vs)/2. - (d2*complex(0,1)*R21*R32*R33*vs)/2. - (3*complex(0,1)*Id1*R31*R32*R33*vs)/2. - (3*complex(0,1)*R21*R22*R23*Rd1*vs)/2. + (3*complex(0,1)*R23*R31*R32*Rd1*vs)/2. + (3*complex(0,1)*R22*R31*R33*Rd1*vs)/2. + (3*complex(0,1)*R21*R32*R33*Rd1*vs)/2. - (3*complex(0,1)*R21*R22*R23*Rd3*vs)/2. + (3*R22*R23*R31*Rd3*vs)/4. + (3*R21*R23*R32*Rd3*vs)/4. + (3*R21*R22*R33*Rd3*vs)/4. + (3*R31*R32*R33*Rd3*vs)/4. - (complex(0,1)*R12*R13*R21*Rdelta3*vs)/2. - (complex(0,1)*R11*R13*R22*Rdelta3*vs)/2. - (complex(0,1)*R11*R12*R23*Rdelta3*vs)/2. + (complex(0,1)*Idelta1*R12*R13*R31)/(2.*cmath.sqrt(2)) + (complex(0,1)*Ic1*R22*R23*R31)/cmath.sqrt(2) + (complex(0,1)*Ic2*R22*R23*R31)/(3.*cmath.sqrt(2)) + (complex(0,1)*Idelta1*R11*R13*R32)/(2.*cmath.sqrt(2)) + (complex(0,1)*Ic1*R21*R23*R32)/cmath.sqrt(2) + (complex(0,1)*Ic2*R21*R23*R32)/(3.*cmath.sqrt(2)) + (complex(0,1)*Idelta1*R11*R12*R33)/(2.*cmath.sqrt(2)) + (complex(0,1)*Ic1*R21*R22*R33)/cmath.sqrt(2) + (complex(0,1)*Ic2*R21*R22*R33)/(3.*cmath.sqrt(2)) - (complex(0,1)*Ic1*R31*R32*R33)/cmath.sqrt(2) + (complex(0,1)*Ic2*R31*R32*R33)/cmath.sqrt(2) - (complex(0,1)*R21*R22*R23*Rc1)/cmath.sqrt(2) + (complex(0,1)*R23*R31*R32*Rc1)/cmath.sqrt(2) + (complex(0,1)*R22*R31*R33*Rc1)/cmath.sqrt(2) + (complex(0,1)*R21*R32*R33*Rc1)/cmath.sqrt(2) - (complex(0,1)*R21*R22*R23*Rc2)/cmath.sqrt(2) - (complex(0,1)*R23*R31*R32*Rc2)/(3.*cmath.sqrt(2)) - (complex(0,1)*R22*R31*R33*Rc2)/(3.*cmath.sqrt(2)) - (complex(0,1)*R21*R32*R33*Rc2)/(3.*cmath.sqrt(2)) - (complex(0,1)*R12*R13*R21*Rdelta1)/(2.*cmath.sqrt(2)) - (complex(0,1)*R11*R13*R22*Rdelta1)/(2.*cmath.sqrt(2)) - (complex(0,1)*R11*R12*R23*Rdelta1)/(2.*cmath.sqrt(2))',
                  order = {'QED':1})

GC_169 = Coupling(name = 'GC_169',
                  value = '-6*complex(0,1)*lam*R12**2*R13*vev - (delta2*complex(0,1)*R13*R22**2*vev)/2. - delta2*complex(0,1)*R12*R22*R23*vev + complex(0,1)*Idelta3*R13*R22*R32*vev + complex(0,1)*Idelta3*R12*R23*R32*vev - (delta2*complex(0,1)*R13*R32**2*vev)/2. + complex(0,1)*Idelta3*R12*R22*R33*vev - delta2*complex(0,1)*R12*R32*R33*vev - (complex(0,1)*R13*R22**2*Rdelta3*vev)/2. - complex(0,1)*R12*R22*R23*Rdelta3*vev + (complex(0,1)*R13*R32**2*Rdelta3*vev)/2. + complex(0,1)*R12*R32*R33*Rdelta3*vev - delta2*complex(0,1)*R12*R13*R22*vs - (delta2*complex(0,1)*R12**2*R23*vs)/2. - (3*d2*complex(0,1)*R22**2*R23*vs)/2. + complex(0,1)*Idelta3*R12*R13*R32*vs + 3*complex(0,1)*Id1*R22*R23*R32*vs - (d2*complex(0,1)*R23*R32**2*vs)/2. + (complex(0,1)*Idelta3*R12**2*R33*vs)/2. + (3*complex(0,1)*Id1*R22**2*R33*vs)/2. - d2*complex(0,1)*R22*R32*R33*vs - (3*complex(0,1)*Id1*R32**2*R33*vs)/2. - (3*complex(0,1)*R22**2*R23*Rd1*vs)/2. + (3*complex(0,1)*R23*R32**2*Rd1*vs)/2. + 3*complex(0,1)*R22*R32*R33*Rd1*vs - (3*complex(0,1)*R22**2*R23*Rd3*vs)/2. + (3*R22*R23*R32*Rd3*vs)/2. + (3*R22**2*R33*Rd3*vs)/4. + (3*R32**2*R33*Rd3*vs)/4. - complex(0,1)*R12*R13*R22*Rdelta3*vs - (complex(0,1)*R12**2*R23*Rdelta3*vs)/2. + (complex(0,1)*Idelta1*R12*R13*R32)/cmath.sqrt(2) + (complex(0,1)*Idelta1*R12**2*R33)/(2.*cmath.sqrt(2)) + (complex(0,1)*Ic1*R22**2*R33)/cmath.sqrt(2) + (complex(0,1)*Ic2*R22**2*R33)/(3.*cmath.sqrt(2)) - (complex(0,1)*Ic1*R32**2*R33)/cmath.sqrt(2) + (complex(0,1)*Ic2*R32**2*R33)/cmath.sqrt(2) - (complex(0,1)*R22**2*R23*Rc1)/cmath.sqrt(2) + (complex(0,1)*R23*R32**2*Rc1)/cmath.sqrt(2) - (complex(0,1)*R22**2*R23*Rc2)/cmath.sqrt(2) - (complex(0,1)*R23*R32**2*Rc2)/(3.*cmath.sqrt(2)) - (complex(0,1)*R12*R13*R22*Rdelta1)/cmath.sqrt(2) - (complex(0,1)*R12**2*R23*Rdelta1)/(2.*cmath.sqrt(2)) + complex(0,1)*Ic1*R22*R23*R32*cmath.sqrt(2) + (complex(0,1)*Ic2*R22*R23*R32*cmath.sqrt(2))/3. + complex(0,1)*R22*R32*R33*Rc1*cmath.sqrt(2) - (complex(0,1)*R22*R32*R33*Rc2*cmath.sqrt(2))/3.',
                  order = {'QED':1})

GC_17 = Coupling(name = 'GC_17',
                 value = 'I1a22',
                 order = {'QED':1})

GC_170 = Coupling(name = 'GC_170',
                  value = '-6*complex(0,1)*lam*R11*R13**2*vev - delta2*complex(0,1)*R13*R21*R23*vev - (delta2*complex(0,1)*R11*R23**2*vev)/2. + complex(0,1)*Idelta3*R13*R23*R31*vev + complex(0,1)*Idelta3*R13*R21*R33*vev + complex(0,1)*Idelta3*R11*R23*R33*vev - delta2*complex(0,1)*R13*R31*R33*vev - (delta2*complex(0,1)*R11*R33**2*vev)/2. - complex(0,1)*R13*R21*R23*Rdelta3*vev - (complex(0,1)*R11*R23**2*Rdelta3*vev)/2. + complex(0,1)*R13*R31*R33*Rdelta3*vev + (complex(0,1)*R11*R33**2*Rdelta3*vev)/2. - (delta2*complex(0,1)*R13**2*R21*vs)/2. - delta2*complex(0,1)*R11*R13*R23*vs - (3*d2*complex(0,1)*R21*R23**2*vs)/2. + (complex(0,1)*Idelta3*R13**2*R31*vs)/2. + (3*complex(0,1)*Id1*R23**2*R31*vs)/2. + complex(0,1)*Idelta3*R11*R13*R33*vs + 3*complex(0,1)*Id1*R21*R23*R33*vs - d2*complex(0,1)*R23*R31*R33*vs - (d2*complex(0,1)*R21*R33**2*vs)/2. - (3*complex(0,1)*Id1*R31*R33**2*vs)/2. - (3*complex(0,1)*R21*R23**2*Rd1*vs)/2. + 3*complex(0,1)*R23*R31*R33*Rd1*vs + (3*complex(0,1)*R21*R33**2*Rd1*vs)/2. - (3*complex(0,1)*R21*R23**2*Rd3*vs)/2. + (3*R23**2*R31*Rd3*vs)/4. + (3*R21*R23*R33*Rd3*vs)/2. + (3*R31*R33**2*Rd3*vs)/4. - (complex(0,1)*R13**2*R21*Rdelta3*vs)/2. - complex(0,1)*R11*R13*R23*Rdelta3*vs + (complex(0,1)*Idelta1*R13**2*R31)/(2.*cmath.sqrt(2)) + (complex(0,1)*Ic1*R23**2*R31)/cmath.sqrt(2) + (complex(0,1)*Ic2*R23**2*R31)/(3.*cmath.sqrt(2)) + (complex(0,1)*Idelta1*R11*R13*R33)/cmath.sqrt(2) - (complex(0,1)*Ic1*R31*R33**2)/cmath.sqrt(2) + (complex(0,1)*Ic2*R31*R33**2)/cmath.sqrt(2) - (complex(0,1)*R21*R23**2*Rc1)/cmath.sqrt(2) + (complex(0,1)*R21*R33**2*Rc1)/cmath.sqrt(2) - (complex(0,1)*R21*R23**2*Rc2)/cmath.sqrt(2) - (complex(0,1)*R21*R33**2*Rc2)/(3.*cmath.sqrt(2)) - (complex(0,1)*R13**2*R21*Rdelta1)/(2.*cmath.sqrt(2)) - (complex(0,1)*R11*R13*R23*Rdelta1)/cmath.sqrt(2) + complex(0,1)*Ic1*R21*R23*R33*cmath.sqrt(2) + (complex(0,1)*Ic2*R21*R23*R33*cmath.sqrt(2))/3. + complex(0,1)*R23*R31*R33*Rc1*cmath.sqrt(2) - (complex(0,1)*R23*R31*R33*Rc2*cmath.sqrt(2))/3.',
                  order = {'QED':1})

GC_171 = Coupling(name = 'GC_171',
                  value = '-6*complex(0,1)*lam*R12*R13**2*vev - delta2*complex(0,1)*R13*R22*R23*vev - (delta2*complex(0,1)*R12*R23**2*vev)/2. + complex(0,1)*Idelta3*R13*R23*R32*vev + complex(0,1)*Idelta3*R13*R22*R33*vev + complex(0,1)*Idelta3*R12*R23*R33*vev - delta2*complex(0,1)*R13*R32*R33*vev - (delta2*complex(0,1)*R12*R33**2*vev)/2. - complex(0,1)*R13*R22*R23*Rdelta3*vev - (complex(0,1)*R12*R23**2*Rdelta3*vev)/2. + complex(0,1)*R13*R32*R33*Rdelta3*vev + (complex(0,1)*R12*R33**2*Rdelta3*vev)/2. - (delta2*complex(0,1)*R13**2*R22*vs)/2. - delta2*complex(0,1)*R12*R13*R23*vs - (3*d2*complex(0,1)*R22*R23**2*vs)/2. + (complex(0,1)*Idelta3*R13**2*R32*vs)/2. + (3*complex(0,1)*Id1*R23**2*R32*vs)/2. + complex(0,1)*Idelta3*R12*R13*R33*vs + 3*complex(0,1)*Id1*R22*R23*R33*vs - d2*complex(0,1)*R23*R32*R33*vs - (d2*complex(0,1)*R22*R33**2*vs)/2. - (3*complex(0,1)*Id1*R32*R33**2*vs)/2. - (3*complex(0,1)*R22*R23**2*Rd1*vs)/2. + 3*complex(0,1)*R23*R32*R33*Rd1*vs + (3*complex(0,1)*R22*R33**2*Rd1*vs)/2. - (3*complex(0,1)*R22*R23**2*Rd3*vs)/2. + (3*R23**2*R32*Rd3*vs)/4. + (3*R22*R23*R33*Rd3*vs)/2. + (3*R32*R33**2*Rd3*vs)/4. - (complex(0,1)*R13**2*R22*Rdelta3*vs)/2. - complex(0,1)*R12*R13*R23*Rdelta3*vs + (complex(0,1)*Idelta1*R13**2*R32)/(2.*cmath.sqrt(2)) + (complex(0,1)*Ic1*R23**2*R32)/cmath.sqrt(2) + (complex(0,1)*Ic2*R23**2*R32)/(3.*cmath.sqrt(2)) + (complex(0,1)*Idelta1*R12*R13*R33)/cmath.sqrt(2) - (complex(0,1)*Ic1*R32*R33**2)/cmath.sqrt(2) + (complex(0,1)*Ic2*R32*R33**2)/cmath.sqrt(2) - (complex(0,1)*R22*R23**2*Rc1)/cmath.sqrt(2) + (complex(0,1)*R22*R33**2*Rc1)/cmath.sqrt(2) - (complex(0,1)*R22*R23**2*Rc2)/cmath.sqrt(2) - (complex(0,1)*R22*R33**2*Rc2)/(3.*cmath.sqrt(2)) - (complex(0,1)*R13**2*R22*Rdelta1)/(2.*cmath.sqrt(2)) - (complex(0,1)*R12*R13*R23*Rdelta1)/cmath.sqrt(2) + complex(0,1)*Ic1*R22*R23*R33*cmath.sqrt(2) + (complex(0,1)*Ic2*R22*R23*R33*cmath.sqrt(2))/3. + complex(0,1)*R23*R32*R33*Rc1*cmath.sqrt(2) - (complex(0,1)*R23*R32*R33*Rc2*cmath.sqrt(2))/3.',
                  order = {'QED':1})

GC_172 = Coupling(name = 'GC_172',
                  value = '-6*complex(0,1)*lam*R13**3*vev - (3*delta2*complex(0,1)*R13*R23**2*vev)/2. + 3*complex(0,1)*Idelta3*R13*R23*R33*vev - (3*delta2*complex(0,1)*R13*R33**2*vev)/2. - (3*complex(0,1)*R13*R23**2*Rdelta3*vev)/2. + (3*complex(0,1)*R13*R33**2*Rdelta3*vev)/2. - (3*delta2*complex(0,1)*R13**2*R23*vs)/2. - (3*d2*complex(0,1)*R23**3*vs)/2. + (3*complex(0,1)*Idelta3*R13**2*R33*vs)/2. + (9*complex(0,1)*Id1*R23**2*R33*vs)/2. - (3*d2*complex(0,1)*R23*R33**2*vs)/2. - (3*complex(0,1)*Id1*R33**3*vs)/2. - (3*complex(0,1)*R23**3*Rd1*vs)/2. + (9*complex(0,1)*R23*R33**2*Rd1*vs)/2. - (3*complex(0,1)*R23**3*Rd3*vs)/2. + (9*R23**2*R33*Rd3*vs)/4. + (3*R33**3*Rd3*vs)/4. - (3*complex(0,1)*R13**2*R23*Rdelta3*vs)/2. + (3*complex(0,1)*Idelta1*R13**2*R33)/(2.*cmath.sqrt(2)) + (3*complex(0,1)*Ic1*R23**2*R33)/cmath.sqrt(2) + (complex(0,1)*Ic2*R23**2*R33)/cmath.sqrt(2) - (complex(0,1)*Ic1*R33**3)/cmath.sqrt(2) + (complex(0,1)*Ic2*R33**3)/cmath.sqrt(2) - (complex(0,1)*R23**3*Rc1)/cmath.sqrt(2) + (3*complex(0,1)*R23*R33**2*Rc1)/cmath.sqrt(2) - (complex(0,1)*R23**3*Rc2)/cmath.sqrt(2) - (complex(0,1)*R23*R33**2*Rc2)/cmath.sqrt(2) - (3*complex(0,1)*R13**2*R23*Rdelta1)/(2.*cmath.sqrt(2))',
                  order = {'QED':1})

GC_173 = Coupling(name = 'GC_173',
                  value = '-(yb/cmath.sqrt(2))',
                  order = {'QED':1})

GC_174 = Coupling(name = 'GC_174',
                  value = 'yb/cmath.sqrt(2)',
                  order = {'QED':1})

GC_175 = Coupling(name = 'GC_175',
                  value = '-((complex(0,1)*R11*yb)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_176 = Coupling(name = 'GC_176',
                  value = '-((complex(0,1)*R12*yb)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_177 = Coupling(name = 'GC_177',
                  value = '-((complex(0,1)*R13*yb)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_178 = Coupling(name = 'GC_178',
                  value = '-(yc/cmath.sqrt(2))',
                  order = {'QED':1})

GC_179 = Coupling(name = 'GC_179',
                  value = 'yc/cmath.sqrt(2)',
                  order = {'QED':1})

GC_18 = Coupling(name = 'GC_18',
                 value = 'I1a23',
                 order = {'QED':1})

GC_180 = Coupling(name = 'GC_180',
                  value = '-((complex(0,1)*R11*yc)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_181 = Coupling(name = 'GC_181',
                  value = '-((complex(0,1)*R12*yc)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_182 = Coupling(name = 'GC_182',
                  value = '-((complex(0,1)*R13*yc)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_183 = Coupling(name = 'GC_183',
                  value = '-(ydo/cmath.sqrt(2))',
                  order = {'QED':1})

GC_184 = Coupling(name = 'GC_184',
                  value = 'ydo/cmath.sqrt(2)',
                  order = {'QED':1})

GC_185 = Coupling(name = 'GC_185',
                  value = '-((complex(0,1)*R11*ydo)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_186 = Coupling(name = 'GC_186',
                  value = '-((complex(0,1)*R12*ydo)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_187 = Coupling(name = 'GC_187',
                  value = '-((complex(0,1)*R13*ydo)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_188 = Coupling(name = 'GC_188',
                  value = '-ye',
                  order = {'QED':1})

GC_189 = Coupling(name = 'GC_189',
                  value = 'ye',
                  order = {'QED':1})

GC_19 = Coupling(name = 'GC_19',
                 value = 'I1a31',
                 order = {'QED':1})

GC_190 = Coupling(name = 'GC_190',
                  value = '-(ye/cmath.sqrt(2))',
                  order = {'QED':1})

GC_191 = Coupling(name = 'GC_191',
                  value = 'ye/cmath.sqrt(2)',
                  order = {'QED':1})

GC_192 = Coupling(name = 'GC_192',
                  value = '-((complex(0,1)*R11*ye)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_193 = Coupling(name = 'GC_193',
                  value = '-((complex(0,1)*R12*ye)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_194 = Coupling(name = 'GC_194',
                  value = '-((complex(0,1)*R13*ye)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_195 = Coupling(name = 'GC_195',
                  value = '-ym',
                  order = {'QED':1})

GC_196 = Coupling(name = 'GC_196',
                  value = 'ym',
                  order = {'QED':1})

GC_197 = Coupling(name = 'GC_197',
                  value = '-(ym/cmath.sqrt(2))',
                  order = {'QED':1})

GC_198 = Coupling(name = 'GC_198',
                  value = 'ym/cmath.sqrt(2)',
                  order = {'QED':1})

GC_199 = Coupling(name = 'GC_199',
                  value = '-((complex(0,1)*R11*ym)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_2 = Coupling(name = 'GC_2',
                value = '(2*ee*complex(0,1))/3.',
                order = {'QED':1})

GC_20 = Coupling(name = 'GC_20',
                 value = 'I1a32',
                 order = {'QED':1})

GC_200 = Coupling(name = 'GC_200',
                  value = '-((complex(0,1)*R12*ym)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_201 = Coupling(name = 'GC_201',
                  value = '-((complex(0,1)*R13*ym)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_202 = Coupling(name = 'GC_202',
                  value = '-(ys/cmath.sqrt(2))',
                  order = {'QED':1})

GC_203 = Coupling(name = 'GC_203',
                  value = 'ys/cmath.sqrt(2)',
                  order = {'QED':1})

GC_204 = Coupling(name = 'GC_204',
                  value = '-((complex(0,1)*R11*ys)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_205 = Coupling(name = 'GC_205',
                  value = '-((complex(0,1)*R12*ys)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_206 = Coupling(name = 'GC_206',
                  value = '-((complex(0,1)*R13*ys)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_207 = Coupling(name = 'GC_207',
                  value = '-(yt/cmath.sqrt(2))',
                  order = {'QED':1})

GC_208 = Coupling(name = 'GC_208',
                  value = 'yt/cmath.sqrt(2)',
                  order = {'QED':1})

GC_209 = Coupling(name = 'GC_209',
                  value = '-((complex(0,1)*R11*yt)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_21 = Coupling(name = 'GC_21',
                 value = 'I1a33',
                 order = {'QED':1})

GC_210 = Coupling(name = 'GC_210',
                  value = '-((complex(0,1)*R12*yt)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_211 = Coupling(name = 'GC_211',
                  value = '-((complex(0,1)*R13*yt)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_212 = Coupling(name = 'GC_212',
                  value = '-ytau',
                  order = {'QED':1})

GC_213 = Coupling(name = 'GC_213',
                  value = 'ytau',
                  order = {'QED':1})

GC_214 = Coupling(name = 'GC_214',
                  value = '-(ytau/cmath.sqrt(2))',
                  order = {'QED':1})

GC_215 = Coupling(name = 'GC_215',
                  value = 'ytau/cmath.sqrt(2)',
                  order = {'QED':1})

GC_216 = Coupling(name = 'GC_216',
                  value = '-((complex(0,1)*R11*ytau)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_217 = Coupling(name = 'GC_217',
                  value = '-((complex(0,1)*R12*ytau)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_218 = Coupling(name = 'GC_218',
                  value = '-((complex(0,1)*R13*ytau)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_219 = Coupling(name = 'GC_219',
                  value = '-(yup/cmath.sqrt(2))',
                  order = {'QED':1})

GC_22 = Coupling(name = 'GC_22',
                 value = '-I2a11',
                 order = {'QED':1})

GC_220 = Coupling(name = 'GC_220',
                  value = 'yup/cmath.sqrt(2)',
                  order = {'QED':1})

GC_221 = Coupling(name = 'GC_221',
                  value = '-((complex(0,1)*R11*yup)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_222 = Coupling(name = 'GC_222',
                  value = '-((complex(0,1)*R12*yup)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_223 = Coupling(name = 'GC_223',
                  value = '-((complex(0,1)*R13*yup)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_224 = Coupling(name = 'GC_224',
                  value = '(ee*complex(0,1)*complexconjugate(CKM1x1))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_225 = Coupling(name = 'GC_225',
                  value = '(ee*complex(0,1)*complexconjugate(CKM1x2))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_226 = Coupling(name = 'GC_226',
                  value = '(ee*complex(0,1)*complexconjugate(CKM1x3))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_227 = Coupling(name = 'GC_227',
                  value = '(ee*complex(0,1)*complexconjugate(CKM2x1))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_228 = Coupling(name = 'GC_228',
                  value = '(ee*complex(0,1)*complexconjugate(CKM2x2))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_229 = Coupling(name = 'GC_229',
                  value = '(ee*complex(0,1)*complexconjugate(CKM2x3))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_23 = Coupling(name = 'GC_23',
                 value = '-I2a12',
                 order = {'QED':1})

GC_230 = Coupling(name = 'GC_230',
                  value = '(ee*complex(0,1)*complexconjugate(CKM3x1))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_231 = Coupling(name = 'GC_231',
                  value = '(ee*complex(0,1)*complexconjugate(CKM3x2))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_232 = Coupling(name = 'GC_232',
                  value = '(ee*complex(0,1)*complexconjugate(CKM3x3))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_24 = Coupling(name = 'GC_24',
                 value = '-I2a13',
                 order = {'QED':1})

GC_25 = Coupling(name = 'GC_25',
                 value = '-I2a21',
                 order = {'QED':1})

GC_26 = Coupling(name = 'GC_26',
                 value = '-I2a22',
                 order = {'QED':1})

GC_27 = Coupling(name = 'GC_27',
                 value = '-I2a23',
                 order = {'QED':1})

GC_28 = Coupling(name = 'GC_28',
                 value = '-I2a31',
                 order = {'QED':1})

GC_29 = Coupling(name = 'GC_29',
                 value = '-I2a32',
                 order = {'QED':1})

GC_3 = Coupling(name = 'GC_3',
                value = '-(ee*complex(0,1))',
                order = {'QED':1})

GC_30 = Coupling(name = 'GC_30',
                 value = '-I2a33',
                 order = {'QED':1})

GC_31 = Coupling(name = 'GC_31',
                 value = 'I3a11',
                 order = {'QED':1})

GC_32 = Coupling(name = 'GC_32',
                 value = 'I3a12',
                 order = {'QED':1})

GC_33 = Coupling(name = 'GC_33',
                 value = 'I3a13',
                 order = {'QED':1})

GC_34 = Coupling(name = 'GC_34',
                 value = 'I3a21',
                 order = {'QED':1})

GC_35 = Coupling(name = 'GC_35',
                 value = 'I3a22',
                 order = {'QED':1})

GC_36 = Coupling(name = 'GC_36',
                 value = 'I3a23',
                 order = {'QED':1})

GC_37 = Coupling(name = 'GC_37',
                 value = 'I3a31',
                 order = {'QED':1})

GC_38 = Coupling(name = 'GC_38',
                 value = 'I3a32',
                 order = {'QED':1})

GC_39 = Coupling(name = 'GC_39',
                 value = 'I3a33',
                 order = {'QED':1})

GC_4 = Coupling(name = 'GC_4',
                value = 'ee*complex(0,1)',
                order = {'QED':1})

GC_40 = Coupling(name = 'GC_40',
                 value = '-I4a11',
                 order = {'QED':1})

GC_41 = Coupling(name = 'GC_41',
                 value = '-I4a12',
                 order = {'QED':1})

GC_42 = Coupling(name = 'GC_42',
                 value = '-I4a13',
                 order = {'QED':1})

GC_43 = Coupling(name = 'GC_43',
                 value = '-I4a21',
                 order = {'QED':1})

GC_44 = Coupling(name = 'GC_44',
                 value = '-I4a22',
                 order = {'QED':1})

GC_45 = Coupling(name = 'GC_45',
                 value = '-I4a23',
                 order = {'QED':1})

GC_46 = Coupling(name = 'GC_46',
                 value = '-I4a31',
                 order = {'QED':1})

GC_47 = Coupling(name = 'GC_47',
                 value = '-I4a32',
                 order = {'QED':1})

GC_48 = Coupling(name = 'GC_48',
                 value = '-I4a33',
                 order = {'QED':1})

GC_49 = Coupling(name = 'GC_49',
                 value = '-2*complex(0,1)*lam',
                 order = {'QED':2})

GC_5 = Coupling(name = 'GC_5',
                value = 'ee**2*complex(0,1)',
                order = {'QED':2})

GC_50 = Coupling(name = 'GC_50',
                 value = '-4*complex(0,1)*lam',
                 order = {'QED':2})

GC_51 = Coupling(name = 'GC_51',
                 value = '-6*complex(0,1)*lam',
                 order = {'QED':2})

GC_52 = Coupling(name = 'GC_52',
                 value = '-0.5*(ee**2*R11)/cw',
                 order = {'QED':2})

GC_53 = Coupling(name = 'GC_53',
                 value = '(ee**2*R11)/(2.*cw)',
                 order = {'QED':2})

GC_54 = Coupling(name = 'GC_54',
                 value = '-0.5*(ee**2*R12)/cw',
                 order = {'QED':2})

GC_55 = Coupling(name = 'GC_55',
                 value = '(ee**2*R12)/(2.*cw)',
                 order = {'QED':2})

GC_56 = Coupling(name = 'GC_56',
                 value = '-0.5*(ee**2*R13)/cw',
                 order = {'QED':2})

GC_57 = Coupling(name = 'GC_57',
                 value = '(ee**2*R13)/(2.*cw)',
                 order = {'QED':2})

GC_58 = Coupling(name = 'GC_58',
                 value = '-((complex(0,1)*lamX*R21)/cmath.sqrt(2)) - (lamX*R31)/cmath.sqrt(2)',
                 order = {'VLF':1})

GC_59 = Coupling(name = 'GC_59',
                 value = '-((complex(0,1)*lamX*R21)/cmath.sqrt(2)) + (lamX*R31)/cmath.sqrt(2)',
                 order = {'VLF':1})

GC_6 = Coupling(name = 'GC_6',
                value = '2*ee**2*complex(0,1)',
                order = {'QED':2})

GC_60 = Coupling(name = 'GC_60',
                 value = '-((complex(0,1)*lamX*R22)/cmath.sqrt(2)) - (lamX*R32)/cmath.sqrt(2)',
                 order = {'VLF':1})

GC_61 = Coupling(name = 'GC_61',
                 value = '-((complex(0,1)*lamX*R22)/cmath.sqrt(2)) + (lamX*R32)/cmath.sqrt(2)',
                 order = {'VLF':1})

GC_62 = Coupling(name = 'GC_62',
                 value = '-((complex(0,1)*lamX*R23)/cmath.sqrt(2)) - (lamX*R33)/cmath.sqrt(2)',
                 order = {'VLF':1})

GC_63 = Coupling(name = 'GC_63',
                 value = '-((complex(0,1)*lamX*R23)/cmath.sqrt(2)) + (lamX*R33)/cmath.sqrt(2)',
                 order = {'VLF':1})

GC_64 = Coupling(name = 'GC_64',
                 value = '-2*complex(0,1)*lam*R11**2 - (delta2*complex(0,1)*R21**2)/2. + complex(0,1)*Idelta3*R21*R31 - (delta2*complex(0,1)*R31**2)/2. - (complex(0,1)*R21**2*Rdelta3)/2. + (complex(0,1)*R31**2*Rdelta3)/2.',
                 order = {'QED':2})

GC_65 = Coupling(name = 'GC_65',
                 value = '-6*complex(0,1)*lam*R11**4 - 3*delta2*complex(0,1)*R11**2*R21**2 - (3*d2*complex(0,1)*R21**4)/2. + 6*complex(0,1)*Idelta3*R11**2*R21*R31 + 6*complex(0,1)*Id1*R21**3*R31 - 3*delta2*complex(0,1)*R11**2*R31**2 - 3*d2*complex(0,1)*R21**2*R31**2 - 6*complex(0,1)*Id1*R21*R31**3 - (3*d2*complex(0,1)*R31**4)/2. - (3*complex(0,1)*R21**4*Rd1)/2. + 9*complex(0,1)*R21**2*R31**2*Rd1 - (3*complex(0,1)*R31**4*Rd1)/2. - (3*complex(0,1)*R21**4*Rd3)/2. + 3*R21**3*R31*Rd3 + 3*R21*R31**3*Rd3 + (3*complex(0,1)*R31**4*Rd3)/2. - 3*complex(0,1)*R11**2*R21**2*Rdelta3 + 3*complex(0,1)*R11**2*R31**2*Rdelta3',
                 order = {'QED':2})

GC_66 = Coupling(name = 'GC_66',
                 value = '-2*complex(0,1)*lam*R11*R12 - (delta2*complex(0,1)*R21*R22)/2. + (complex(0,1)*Idelta3*R22*R31)/2. + (complex(0,1)*Idelta3*R21*R32)/2. - (delta2*complex(0,1)*R31*R32)/2. - (complex(0,1)*R21*R22*Rdelta3)/2. + (complex(0,1)*R31*R32*Rdelta3)/2.',
                 order = {'QED':2})

GC_67 = Coupling(name = 'GC_67',
                 value = '-6*complex(0,1)*lam*R11**3*R12 - (3*delta2*complex(0,1)*R11*R12*R21**2)/2. - (3*delta2*complex(0,1)*R11**2*R21*R22)/2. - (3*d2*complex(0,1)*R21**3*R22)/2. + 3*complex(0,1)*Idelta3*R11*R12*R21*R31 + (3*complex(0,1)*Idelta3*R11**2*R22*R31)/2. + (9*complex(0,1)*Id1*R21**2*R22*R31)/2. - (3*delta2*complex(0,1)*R11*R12*R31**2)/2. - (3*d2*complex(0,1)*R21*R22*R31**2)/2. - (3*complex(0,1)*Id1*R22*R31**3)/2. + (3*complex(0,1)*Idelta3*R11**2*R21*R32)/2. + (3*complex(0,1)*Id1*R21**3*R32)/2. - (3*delta2*complex(0,1)*R11**2*R31*R32)/2. - (3*d2*complex(0,1)*R21**2*R31*R32)/2. - (9*complex(0,1)*Id1*R21*R31**2*R32)/2. - (3*d2*complex(0,1)*R31**3*R32)/2. - (3*complex(0,1)*R21**3*R22*Rd1)/2. + (9*complex(0,1)*R21*R22*R31**2*Rd1)/2. + (9*complex(0,1)*R21**2*R31*R32*Rd1)/2. - (3*complex(0,1)*R31**3*R32*Rd1)/2. - (3*complex(0,1)*R21**3*R22*Rd3)/2. + (9*R21**2*R22*R31*Rd3)/4. + (3*R22*R31**3*Rd3)/4. + (3*R21**3*R32*Rd3)/4. + (9*R21*R31**2*R32*Rd3)/4. + (3*complex(0,1)*R31**3*R32*Rd3)/2. - (3*complex(0,1)*R11*R12*R21**2*Rdelta3)/2. - (3*complex(0,1)*R11**2*R21*R22*Rdelta3)/2. + (3*complex(0,1)*R11*R12*R31**2*Rdelta3)/2. + (3*complex(0,1)*R11**2*R31*R32*Rdelta3)/2.',
                 order = {'QED':2})

GC_68 = Coupling(name = 'GC_68',
                 value = '-2*complex(0,1)*lam*R12**2 - (delta2*complex(0,1)*R22**2)/2. + complex(0,1)*Idelta3*R22*R32 - (delta2*complex(0,1)*R32**2)/2. - (complex(0,1)*R22**2*Rdelta3)/2. + (complex(0,1)*R32**2*Rdelta3)/2.',
                 order = {'QED':2})

GC_69 = Coupling(name = 'GC_69',
                 value = '-6*complex(0,1)*lam*R11**2*R12**2 - (delta2*complex(0,1)*R12**2*R21**2)/2. - 2*delta2*complex(0,1)*R11*R12*R21*R22 - (delta2*complex(0,1)*R11**2*R22**2)/2. - (3*d2*complex(0,1)*R21**2*R22**2)/2. + complex(0,1)*Idelta3*R12**2*R21*R31 + 2*complex(0,1)*Idelta3*R11*R12*R22*R31 + 3*complex(0,1)*Id1*R21*R22**2*R31 - (delta2*complex(0,1)*R12**2*R31**2)/2. - (d2*complex(0,1)*R22**2*R31**2)/2. + 2*complex(0,1)*Idelta3*R11*R12*R21*R32 + complex(0,1)*Idelta3*R11**2*R22*R32 + 3*complex(0,1)*Id1*R21**2*R22*R32 - 2*delta2*complex(0,1)*R11*R12*R31*R32 - 2*d2*complex(0,1)*R21*R22*R31*R32 - 3*complex(0,1)*Id1*R22*R31**2*R32 - (delta2*complex(0,1)*R11**2*R32**2)/2. - (d2*complex(0,1)*R21**2*R32**2)/2. - 3*complex(0,1)*Id1*R21*R31*R32**2 - (3*d2*complex(0,1)*R31**2*R32**2)/2. - (3*complex(0,1)*R21**2*R22**2*Rd1)/2. + (3*complex(0,1)*R22**2*R31**2*Rd1)/2. + 6*complex(0,1)*R21*R22*R31*R32*Rd1 + (3*complex(0,1)*R21**2*R32**2*Rd1)/2. - (3*complex(0,1)*R31**2*R32**2*Rd1)/2. - (3*complex(0,1)*R21**2*R22**2*Rd3)/2. + (3*R21*R22**2*R31*Rd3)/2. + (3*R21**2*R22*R32*Rd3)/2. + (3*R22*R31**2*R32*Rd3)/2. + (3*R21*R31*R32**2*Rd3)/2. + (3*complex(0,1)*R31**2*R32**2*Rd3)/2. - (complex(0,1)*R12**2*R21**2*Rdelta3)/2. - 2*complex(0,1)*R11*R12*R21*R22*Rdelta3 - (complex(0,1)*R11**2*R22**2*Rdelta3)/2. + (complex(0,1)*R12**2*R31**2*Rdelta3)/2. + 2*complex(0,1)*R11*R12*R31*R32*Rdelta3 + (complex(0,1)*R11**2*R32**2*Rdelta3)/2.',
                 order = {'QED':2})

GC_7 = Coupling(name = 'GC_7',
                value = '(ee**2*complex(0,1))/(2.*cw)',
                order = {'QED':2})

GC_70 = Coupling(name = 'GC_70',
                 value = '-6*complex(0,1)*lam*R11*R12**3 - (3*delta2*complex(0,1)*R12**2*R21*R22)/2. - (3*delta2*complex(0,1)*R11*R12*R22**2)/2. - (3*d2*complex(0,1)*R21*R22**3)/2. + (3*complex(0,1)*Idelta3*R12**2*R22*R31)/2. + (3*complex(0,1)*Id1*R22**3*R31)/2. + (3*complex(0,1)*Idelta3*R12**2*R21*R32)/2. + 3*complex(0,1)*Idelta3*R11*R12*R22*R32 + (9*complex(0,1)*Id1*R21*R22**2*R32)/2. - (3*delta2*complex(0,1)*R12**2*R31*R32)/2. - (3*d2*complex(0,1)*R22**2*R31*R32)/2. - (3*delta2*complex(0,1)*R11*R12*R32**2)/2. - (3*d2*complex(0,1)*R21*R22*R32**2)/2. - (9*complex(0,1)*Id1*R22*R31*R32**2)/2. - (3*complex(0,1)*Id1*R21*R32**3)/2. - (3*d2*complex(0,1)*R31*R32**3)/2. - (3*complex(0,1)*R21*R22**3*Rd1)/2. + (9*complex(0,1)*R22**2*R31*R32*Rd1)/2. + (9*complex(0,1)*R21*R22*R32**2*Rd1)/2. - (3*complex(0,1)*R31*R32**3*Rd1)/2. - (3*complex(0,1)*R21*R22**3*Rd3)/2. + (3*R22**3*R31*Rd3)/4. + (9*R21*R22**2*R32*Rd3)/4. + (9*R22*R31*R32**2*Rd3)/4. + (3*R21*R32**3*Rd3)/4. + (3*complex(0,1)*R31*R32**3*Rd3)/2. - (3*complex(0,1)*R12**2*R21*R22*Rdelta3)/2. - (3*complex(0,1)*R11*R12*R22**2*Rdelta3)/2. + (3*complex(0,1)*R12**2*R31*R32*Rdelta3)/2. + (3*complex(0,1)*R11*R12*R32**2*Rdelta3)/2.',
                 order = {'QED':2})

GC_71 = Coupling(name = 'GC_71',
                 value = '-6*complex(0,1)*lam*R12**4 - 3*delta2*complex(0,1)*R12**2*R22**2 - (3*d2*complex(0,1)*R22**4)/2. + 6*complex(0,1)*Idelta3*R12**2*R22*R32 + 6*complex(0,1)*Id1*R22**3*R32 - 3*delta2*complex(0,1)*R12**2*R32**2 - 3*d2*complex(0,1)*R22**2*R32**2 - 6*complex(0,1)*Id1*R22*R32**3 - (3*d2*complex(0,1)*R32**4)/2. - (3*complex(0,1)*R22**4*Rd1)/2. + 9*complex(0,1)*R22**2*R32**2*Rd1 - (3*complex(0,1)*R32**4*Rd1)/2. - (3*complex(0,1)*R22**4*Rd3)/2. + 3*R22**3*R32*Rd3 + 3*R22*R32**3*Rd3 + (3*complex(0,1)*R32**4*Rd3)/2. - 3*complex(0,1)*R12**2*R22**2*Rdelta3 + 3*complex(0,1)*R12**2*R32**2*Rdelta3',
                 order = {'QED':2})

GC_72 = Coupling(name = 'GC_72',
                 value = '-2*complex(0,1)*lam*R11*R13 - (delta2*complex(0,1)*R21*R23)/2. + (complex(0,1)*Idelta3*R23*R31)/2. + (complex(0,1)*Idelta3*R21*R33)/2. - (delta2*complex(0,1)*R31*R33)/2. - (complex(0,1)*R21*R23*Rdelta3)/2. + (complex(0,1)*R31*R33*Rdelta3)/2.',
                 order = {'QED':2})

GC_73 = Coupling(name = 'GC_73',
                 value = '-6*complex(0,1)*lam*R11**3*R13 - (3*delta2*complex(0,1)*R11*R13*R21**2)/2. - (3*delta2*complex(0,1)*R11**2*R21*R23)/2. - (3*d2*complex(0,1)*R21**3*R23)/2. + 3*complex(0,1)*Idelta3*R11*R13*R21*R31 + (3*complex(0,1)*Idelta3*R11**2*R23*R31)/2. + (9*complex(0,1)*Id1*R21**2*R23*R31)/2. - (3*delta2*complex(0,1)*R11*R13*R31**2)/2. - (3*d2*complex(0,1)*R21*R23*R31**2)/2. - (3*complex(0,1)*Id1*R23*R31**3)/2. + (3*complex(0,1)*Idelta3*R11**2*R21*R33)/2. + (3*complex(0,1)*Id1*R21**3*R33)/2. - (3*delta2*complex(0,1)*R11**2*R31*R33)/2. - (3*d2*complex(0,1)*R21**2*R31*R33)/2. - (9*complex(0,1)*Id1*R21*R31**2*R33)/2. - (3*d2*complex(0,1)*R31**3*R33)/2. - (3*complex(0,1)*R21**3*R23*Rd1)/2. + (9*complex(0,1)*R21*R23*R31**2*Rd1)/2. + (9*complex(0,1)*R21**2*R31*R33*Rd1)/2. - (3*complex(0,1)*R31**3*R33*Rd1)/2. - (3*complex(0,1)*R21**3*R23*Rd3)/2. + (9*R21**2*R23*R31*Rd3)/4. + (3*R23*R31**3*Rd3)/4. + (3*R21**3*R33*Rd3)/4. + (9*R21*R31**2*R33*Rd3)/4. + (3*complex(0,1)*R31**3*R33*Rd3)/2. - (3*complex(0,1)*R11*R13*R21**2*Rdelta3)/2. - (3*complex(0,1)*R11**2*R21*R23*Rdelta3)/2. + (3*complex(0,1)*R11*R13*R31**2*Rdelta3)/2. + (3*complex(0,1)*R11**2*R31*R33*Rdelta3)/2.',
                 order = {'QED':2})

GC_74 = Coupling(name = 'GC_74',
                 value = '-2*complex(0,1)*lam*R12*R13 - (delta2*complex(0,1)*R22*R23)/2. + (complex(0,1)*Idelta3*R23*R32)/2. + (complex(0,1)*Idelta3*R22*R33)/2. - (delta2*complex(0,1)*R32*R33)/2. - (complex(0,1)*R22*R23*Rdelta3)/2. + (complex(0,1)*R32*R33*Rdelta3)/2.',
                 order = {'QED':2})

GC_75 = Coupling(name = 'GC_75',
                 value = '-6*complex(0,1)*lam*R11**2*R12*R13 - (delta2*complex(0,1)*R12*R13*R21**2)/2. - delta2*complex(0,1)*R11*R13*R21*R22 - delta2*complex(0,1)*R11*R12*R21*R23 - (delta2*complex(0,1)*R11**2*R22*R23)/2. - (3*d2*complex(0,1)*R21**2*R22*R23)/2. + complex(0,1)*Idelta3*R12*R13*R21*R31 + complex(0,1)*Idelta3*R11*R13*R22*R31 + complex(0,1)*Idelta3*R11*R12*R23*R31 + 3*complex(0,1)*Id1*R21*R22*R23*R31 - (delta2*complex(0,1)*R12*R13*R31**2)/2. - (d2*complex(0,1)*R22*R23*R31**2)/2. + complex(0,1)*Idelta3*R11*R13*R21*R32 + (complex(0,1)*Idelta3*R11**2*R23*R32)/2. + (3*complex(0,1)*Id1*R21**2*R23*R32)/2. - delta2*complex(0,1)*R11*R13*R31*R32 - d2*complex(0,1)*R21*R23*R31*R32 - (3*complex(0,1)*Id1*R23*R31**2*R32)/2. + complex(0,1)*Idelta3*R11*R12*R21*R33 + (complex(0,1)*Idelta3*R11**2*R22*R33)/2. + (3*complex(0,1)*Id1*R21**2*R22*R33)/2. - delta2*complex(0,1)*R11*R12*R31*R33 - d2*complex(0,1)*R21*R22*R31*R33 - (3*complex(0,1)*Id1*R22*R31**2*R33)/2. - (delta2*complex(0,1)*R11**2*R32*R33)/2. - (d2*complex(0,1)*R21**2*R32*R33)/2. - 3*complex(0,1)*Id1*R21*R31*R32*R33 - (3*d2*complex(0,1)*R31**2*R32*R33)/2. - (3*complex(0,1)*R21**2*R22*R23*Rd1)/2. + (3*complex(0,1)*R22*R23*R31**2*Rd1)/2. + 3*complex(0,1)*R21*R23*R31*R32*Rd1 + 3*complex(0,1)*R21*R22*R31*R33*Rd1 + (3*complex(0,1)*R21**2*R32*R33*Rd1)/2. - (3*complex(0,1)*R31**2*R32*R33*Rd1)/2. - (3*complex(0,1)*R21**2*R22*R23*Rd3)/2. + (3*R21*R22*R23*R31*Rd3)/2. + (3*R21**2*R23*R32*Rd3)/4. + (3*R23*R31**2*R32*Rd3)/4. + (3*R21**2*R22*R33*Rd3)/4. + (3*R22*R31**2*R33*Rd3)/4. + (3*R21*R31*R32*R33*Rd3)/2. + (3*complex(0,1)*R31**2*R32*R33*Rd3)/2. - (complex(0,1)*R12*R13*R21**2*Rdelta3)/2. - complex(0,1)*R11*R13*R21*R22*Rdelta3 - complex(0,1)*R11*R12*R21*R23*Rdelta3 - (complex(0,1)*R11**2*R22*R23*Rdelta3)/2. + (complex(0,1)*R12*R13*R31**2*Rdelta3)/2. + complex(0,1)*R11*R13*R31*R32*Rdelta3 + complex(0,1)*R11*R12*R31*R33*Rdelta3 + (complex(0,1)*R11**2*R32*R33*Rdelta3)/2.',
                 order = {'QED':2})

GC_76 = Coupling(name = 'GC_76',
                 value = '-6*complex(0,1)*lam*R11*R12**2*R13 - delta2*complex(0,1)*R12*R13*R21*R22 - (delta2*complex(0,1)*R11*R13*R22**2)/2. - (delta2*complex(0,1)*R12**2*R21*R23)/2. - delta2*complex(0,1)*R11*R12*R22*R23 - (3*d2*complex(0,1)*R21*R22**2*R23)/2. + complex(0,1)*Idelta3*R12*R13*R22*R31 + (complex(0,1)*Idelta3*R12**2*R23*R31)/2. + (3*complex(0,1)*Id1*R22**2*R23*R31)/2. + complex(0,1)*Idelta3*R12*R13*R21*R32 + complex(0,1)*Idelta3*R11*R13*R22*R32 + complex(0,1)*Idelta3*R11*R12*R23*R32 + 3*complex(0,1)*Id1*R21*R22*R23*R32 - delta2*complex(0,1)*R12*R13*R31*R32 - d2*complex(0,1)*R22*R23*R31*R32 - (delta2*complex(0,1)*R11*R13*R32**2)/2. - (d2*complex(0,1)*R21*R23*R32**2)/2. - (3*complex(0,1)*Id1*R23*R31*R32**2)/2. + (complex(0,1)*Idelta3*R12**2*R21*R33)/2. + complex(0,1)*Idelta3*R11*R12*R22*R33 + (3*complex(0,1)*Id1*R21*R22**2*R33)/2. - (delta2*complex(0,1)*R12**2*R31*R33)/2. - (d2*complex(0,1)*R22**2*R31*R33)/2. - delta2*complex(0,1)*R11*R12*R32*R33 - d2*complex(0,1)*R21*R22*R32*R33 - 3*complex(0,1)*Id1*R22*R31*R32*R33 - (3*complex(0,1)*Id1*R21*R32**2*R33)/2. - (3*d2*complex(0,1)*R31*R32**2*R33)/2. - (3*complex(0,1)*R21*R22**2*R23*Rd1)/2. + 3*complex(0,1)*R22*R23*R31*R32*Rd1 + (3*complex(0,1)*R21*R23*R32**2*Rd1)/2. + (3*complex(0,1)*R22**2*R31*R33*Rd1)/2. + 3*complex(0,1)*R21*R22*R32*R33*Rd1 - (3*complex(0,1)*R31*R32**2*R33*Rd1)/2. - (3*complex(0,1)*R21*R22**2*R23*Rd3)/2. + (3*R22**2*R23*R31*Rd3)/4. + (3*R21*R22*R23*R32*Rd3)/2. + (3*R23*R31*R32**2*Rd3)/4. + (3*R21*R22**2*R33*Rd3)/4. + (3*R22*R31*R32*R33*Rd3)/2. + (3*R21*R32**2*R33*Rd3)/4. + (3*complex(0,1)*R31*R32**2*R33*Rd3)/2. - complex(0,1)*R12*R13*R21*R22*Rdelta3 - (complex(0,1)*R11*R13*R22**2*Rdelta3)/2. - (complex(0,1)*R12**2*R21*R23*Rdelta3)/2. - complex(0,1)*R11*R12*R22*R23*Rdelta3 + complex(0,1)*R12*R13*R31*R32*Rdelta3 + (complex(0,1)*R11*R13*R32**2*Rdelta3)/2. + (complex(0,1)*R12**2*R31*R33*Rdelta3)/2. + complex(0,1)*R11*R12*R32*R33*Rdelta3',
                 order = {'QED':2})

GC_77 = Coupling(name = 'GC_77',
                 value = '-6*complex(0,1)*lam*R12**3*R13 - (3*delta2*complex(0,1)*R12*R13*R22**2)/2. - (3*delta2*complex(0,1)*R12**2*R22*R23)/2. - (3*d2*complex(0,1)*R22**3*R23)/2. + 3*complex(0,1)*Idelta3*R12*R13*R22*R32 + (3*complex(0,1)*Idelta3*R12**2*R23*R32)/2. + (9*complex(0,1)*Id1*R22**2*R23*R32)/2. - (3*delta2*complex(0,1)*R12*R13*R32**2)/2. - (3*d2*complex(0,1)*R22*R23*R32**2)/2. - (3*complex(0,1)*Id1*R23*R32**3)/2. + (3*complex(0,1)*Idelta3*R12**2*R22*R33)/2. + (3*complex(0,1)*Id1*R22**3*R33)/2. - (3*delta2*complex(0,1)*R12**2*R32*R33)/2. - (3*d2*complex(0,1)*R22**2*R32*R33)/2. - (9*complex(0,1)*Id1*R22*R32**2*R33)/2. - (3*d2*complex(0,1)*R32**3*R33)/2. - (3*complex(0,1)*R22**3*R23*Rd1)/2. + (9*complex(0,1)*R22*R23*R32**2*Rd1)/2. + (9*complex(0,1)*R22**2*R32*R33*Rd1)/2. - (3*complex(0,1)*R32**3*R33*Rd1)/2. - (3*complex(0,1)*R22**3*R23*Rd3)/2. + (9*R22**2*R23*R32*Rd3)/4. + (3*R23*R32**3*Rd3)/4. + (3*R22**3*R33*Rd3)/4. + (9*R22*R32**2*R33*Rd3)/4. + (3*complex(0,1)*R32**3*R33*Rd3)/2. - (3*complex(0,1)*R12*R13*R22**2*Rdelta3)/2. - (3*complex(0,1)*R12**2*R22*R23*Rdelta3)/2. + (3*complex(0,1)*R12*R13*R32**2*Rdelta3)/2. + (3*complex(0,1)*R12**2*R32*R33*Rdelta3)/2.',
                 order = {'QED':2})

GC_78 = Coupling(name = 'GC_78',
                 value = '-2*complex(0,1)*lam*R13**2 - (delta2*complex(0,1)*R23**2)/2. + complex(0,1)*Idelta3*R23*R33 - (delta2*complex(0,1)*R33**2)/2. - (complex(0,1)*R23**2*Rdelta3)/2. + (complex(0,1)*R33**2*Rdelta3)/2.',
                 order = {'QED':2})

GC_79 = Coupling(name = 'GC_79',
                 value = '-6*complex(0,1)*lam*R11**2*R13**2 - (delta2*complex(0,1)*R13**2*R21**2)/2. - 2*delta2*complex(0,1)*R11*R13*R21*R23 - (delta2*complex(0,1)*R11**2*R23**2)/2. - (3*d2*complex(0,1)*R21**2*R23**2)/2. + complex(0,1)*Idelta3*R13**2*R21*R31 + 2*complex(0,1)*Idelta3*R11*R13*R23*R31 + 3*complex(0,1)*Id1*R21*R23**2*R31 - (delta2*complex(0,1)*R13**2*R31**2)/2. - (d2*complex(0,1)*R23**2*R31**2)/2. + 2*complex(0,1)*Idelta3*R11*R13*R21*R33 + complex(0,1)*Idelta3*R11**2*R23*R33 + 3*complex(0,1)*Id1*R21**2*R23*R33 - 2*delta2*complex(0,1)*R11*R13*R31*R33 - 2*d2*complex(0,1)*R21*R23*R31*R33 - 3*complex(0,1)*Id1*R23*R31**2*R33 - (delta2*complex(0,1)*R11**2*R33**2)/2. - (d2*complex(0,1)*R21**2*R33**2)/2. - 3*complex(0,1)*Id1*R21*R31*R33**2 - (3*d2*complex(0,1)*R31**2*R33**2)/2. - (3*complex(0,1)*R21**2*R23**2*Rd1)/2. + (3*complex(0,1)*R23**2*R31**2*Rd1)/2. + 6*complex(0,1)*R21*R23*R31*R33*Rd1 + (3*complex(0,1)*R21**2*R33**2*Rd1)/2. - (3*complex(0,1)*R31**2*R33**2*Rd1)/2. - (3*complex(0,1)*R21**2*R23**2*Rd3)/2. + (3*R21*R23**2*R31*Rd3)/2. + (3*R21**2*R23*R33*Rd3)/2. + (3*R23*R31**2*R33*Rd3)/2. + (3*R21*R31*R33**2*Rd3)/2. + (3*complex(0,1)*R31**2*R33**2*Rd3)/2. - (complex(0,1)*R13**2*R21**2*Rdelta3)/2. - 2*complex(0,1)*R11*R13*R21*R23*Rdelta3 - (complex(0,1)*R11**2*R23**2*Rdelta3)/2. + (complex(0,1)*R13**2*R31**2*Rdelta3)/2. + 2*complex(0,1)*R11*R13*R31*R33*Rdelta3 + (complex(0,1)*R11**2*R33**2*Rdelta3)/2.',
                 order = {'QED':2})

GC_8 = Coupling(name = 'GC_8',
                value = '-G',
                order = {'QCD':1})

GC_80 = Coupling(name = 'GC_80',
                 value = '-6*complex(0,1)*lam*R11*R12*R13**2 - (delta2*complex(0,1)*R13**2*R21*R22)/2. - delta2*complex(0,1)*R12*R13*R21*R23 - delta2*complex(0,1)*R11*R13*R22*R23 - (delta2*complex(0,1)*R11*R12*R23**2)/2. - (3*d2*complex(0,1)*R21*R22*R23**2)/2. + (complex(0,1)*Idelta3*R13**2*R22*R31)/2. + complex(0,1)*Idelta3*R12*R13*R23*R31 + (3*complex(0,1)*Id1*R22*R23**2*R31)/2. + (complex(0,1)*Idelta3*R13**2*R21*R32)/2. + complex(0,1)*Idelta3*R11*R13*R23*R32 + (3*complex(0,1)*Id1*R21*R23**2*R32)/2. - (delta2*complex(0,1)*R13**2*R31*R32)/2. - (d2*complex(0,1)*R23**2*R31*R32)/2. + complex(0,1)*Idelta3*R12*R13*R21*R33 + complex(0,1)*Idelta3*R11*R13*R22*R33 + complex(0,1)*Idelta3*R11*R12*R23*R33 + 3*complex(0,1)*Id1*R21*R22*R23*R33 - delta2*complex(0,1)*R12*R13*R31*R33 - d2*complex(0,1)*R22*R23*R31*R33 - delta2*complex(0,1)*R11*R13*R32*R33 - d2*complex(0,1)*R21*R23*R32*R33 - 3*complex(0,1)*Id1*R23*R31*R32*R33 - (delta2*complex(0,1)*R11*R12*R33**2)/2. - (d2*complex(0,1)*R21*R22*R33**2)/2. - (3*complex(0,1)*Id1*R22*R31*R33**2)/2. - (3*complex(0,1)*Id1*R21*R32*R33**2)/2. - (3*d2*complex(0,1)*R31*R32*R33**2)/2. - (3*complex(0,1)*R21*R22*R23**2*Rd1)/2. + (3*complex(0,1)*R23**2*R31*R32*Rd1)/2. + 3*complex(0,1)*R22*R23*R31*R33*Rd1 + 3*complex(0,1)*R21*R23*R32*R33*Rd1 + (3*complex(0,1)*R21*R22*R33**2*Rd1)/2. - (3*complex(0,1)*R31*R32*R33**2*Rd1)/2. - (3*complex(0,1)*R21*R22*R23**2*Rd3)/2. + (3*R22*R23**2*R31*Rd3)/4. + (3*R21*R23**2*R32*Rd3)/4. + (3*R21*R22*R23*R33*Rd3)/2. + (3*R23*R31*R32*R33*Rd3)/2. + (3*R22*R31*R33**2*Rd3)/4. + (3*R21*R32*R33**2*Rd3)/4. + (3*complex(0,1)*R31*R32*R33**2*Rd3)/2. - (complex(0,1)*R13**2*R21*R22*Rdelta3)/2. - complex(0,1)*R12*R13*R21*R23*Rdelta3 - complex(0,1)*R11*R13*R22*R23*Rdelta3 - (complex(0,1)*R11*R12*R23**2*Rdelta3)/2. + (complex(0,1)*R13**2*R31*R32*Rdelta3)/2. + complex(0,1)*R12*R13*R31*R33*Rdelta3 + complex(0,1)*R11*R13*R32*R33*Rdelta3 + (complex(0,1)*R11*R12*R33**2*Rdelta3)/2.',
                 order = {'QED':2})

GC_81 = Coupling(name = 'GC_81',
                 value = '-6*complex(0,1)*lam*R12**2*R13**2 - (delta2*complex(0,1)*R13**2*R22**2)/2. - 2*delta2*complex(0,1)*R12*R13*R22*R23 - (delta2*complex(0,1)*R12**2*R23**2)/2. - (3*d2*complex(0,1)*R22**2*R23**2)/2. + complex(0,1)*Idelta3*R13**2*R22*R32 + 2*complex(0,1)*Idelta3*R12*R13*R23*R32 + 3*complex(0,1)*Id1*R22*R23**2*R32 - (delta2*complex(0,1)*R13**2*R32**2)/2. - (d2*complex(0,1)*R23**2*R32**2)/2. + 2*complex(0,1)*Idelta3*R12*R13*R22*R33 + complex(0,1)*Idelta3*R12**2*R23*R33 + 3*complex(0,1)*Id1*R22**2*R23*R33 - 2*delta2*complex(0,1)*R12*R13*R32*R33 - 2*d2*complex(0,1)*R22*R23*R32*R33 - 3*complex(0,1)*Id1*R23*R32**2*R33 - (delta2*complex(0,1)*R12**2*R33**2)/2. - (d2*complex(0,1)*R22**2*R33**2)/2. - 3*complex(0,1)*Id1*R22*R32*R33**2 - (3*d2*complex(0,1)*R32**2*R33**2)/2. - (3*complex(0,1)*R22**2*R23**2*Rd1)/2. + (3*complex(0,1)*R23**2*R32**2*Rd1)/2. + 6*complex(0,1)*R22*R23*R32*R33*Rd1 + (3*complex(0,1)*R22**2*R33**2*Rd1)/2. - (3*complex(0,1)*R32**2*R33**2*Rd1)/2. - (3*complex(0,1)*R22**2*R23**2*Rd3)/2. + (3*R22*R23**2*R32*Rd3)/2. + (3*R22**2*R23*R33*Rd3)/2. + (3*R23*R32**2*R33*Rd3)/2. + (3*R22*R32*R33**2*Rd3)/2. + (3*complex(0,1)*R32**2*R33**2*Rd3)/2. - (complex(0,1)*R13**2*R22**2*Rdelta3)/2. - 2*complex(0,1)*R12*R13*R22*R23*Rdelta3 - (complex(0,1)*R12**2*R23**2*Rdelta3)/2. + (complex(0,1)*R13**2*R32**2*Rdelta3)/2. + 2*complex(0,1)*R12*R13*R32*R33*Rdelta3 + (complex(0,1)*R12**2*R33**2*Rdelta3)/2.',
                 order = {'QED':2})

GC_82 = Coupling(name = 'GC_82',
                 value = '-6*complex(0,1)*lam*R11*R13**3 - (3*delta2*complex(0,1)*R13**2*R21*R23)/2. - (3*delta2*complex(0,1)*R11*R13*R23**2)/2. - (3*d2*complex(0,1)*R21*R23**3)/2. + (3*complex(0,1)*Idelta3*R13**2*R23*R31)/2. + (3*complex(0,1)*Id1*R23**3*R31)/2. + (3*complex(0,1)*Idelta3*R13**2*R21*R33)/2. + 3*complex(0,1)*Idelta3*R11*R13*R23*R33 + (9*complex(0,1)*Id1*R21*R23**2*R33)/2. - (3*delta2*complex(0,1)*R13**2*R31*R33)/2. - (3*d2*complex(0,1)*R23**2*R31*R33)/2. - (3*delta2*complex(0,1)*R11*R13*R33**2)/2. - (3*d2*complex(0,1)*R21*R23*R33**2)/2. - (9*complex(0,1)*Id1*R23*R31*R33**2)/2. - (3*complex(0,1)*Id1*R21*R33**3)/2. - (3*d2*complex(0,1)*R31*R33**3)/2. - (3*complex(0,1)*R21*R23**3*Rd1)/2. + (9*complex(0,1)*R23**2*R31*R33*Rd1)/2. + (9*complex(0,1)*R21*R23*R33**2*Rd1)/2. - (3*complex(0,1)*R31*R33**3*Rd1)/2. - (3*complex(0,1)*R21*R23**3*Rd3)/2. + (3*R23**3*R31*Rd3)/4. + (9*R21*R23**2*R33*Rd3)/4. + (9*R23*R31*R33**2*Rd3)/4. + (3*R21*R33**3*Rd3)/4. + (3*complex(0,1)*R31*R33**3*Rd3)/2. - (3*complex(0,1)*R13**2*R21*R23*Rdelta3)/2. - (3*complex(0,1)*R11*R13*R23**2*Rdelta3)/2. + (3*complex(0,1)*R13**2*R31*R33*Rdelta3)/2. + (3*complex(0,1)*R11*R13*R33**2*Rdelta3)/2.',
                 order = {'QED':2})

GC_83 = Coupling(name = 'GC_83',
                 value = '-6*complex(0,1)*lam*R12*R13**3 - (3*delta2*complex(0,1)*R13**2*R22*R23)/2. - (3*delta2*complex(0,1)*R12*R13*R23**2)/2. - (3*d2*complex(0,1)*R22*R23**3)/2. + (3*complex(0,1)*Idelta3*R13**2*R23*R32)/2. + (3*complex(0,1)*Id1*R23**3*R32)/2. + (3*complex(0,1)*Idelta3*R13**2*R22*R33)/2. + 3*complex(0,1)*Idelta3*R12*R13*R23*R33 + (9*complex(0,1)*Id1*R22*R23**2*R33)/2. - (3*delta2*complex(0,1)*R13**2*R32*R33)/2. - (3*d2*complex(0,1)*R23**2*R32*R33)/2. - (3*delta2*complex(0,1)*R12*R13*R33**2)/2. - (3*d2*complex(0,1)*R22*R23*R33**2)/2. - (9*complex(0,1)*Id1*R23*R32*R33**2)/2. - (3*complex(0,1)*Id1*R22*R33**3)/2. - (3*d2*complex(0,1)*R32*R33**3)/2. - (3*complex(0,1)*R22*R23**3*Rd1)/2. + (9*complex(0,1)*R23**2*R32*R33*Rd1)/2. + (9*complex(0,1)*R22*R23*R33**2*Rd1)/2. - (3*complex(0,1)*R32*R33**3*Rd1)/2. - (3*complex(0,1)*R22*R23**3*Rd3)/2. + (3*R23**3*R32*Rd3)/4. + (9*R22*R23**2*R33*Rd3)/4. + (9*R23*R32*R33**2*Rd3)/4. + (3*R22*R33**3*Rd3)/4. + (3*complex(0,1)*R32*R33**3*Rd3)/2. - (3*complex(0,1)*R13**2*R22*R23*Rdelta3)/2. - (3*complex(0,1)*R12*R13*R23**2*Rdelta3)/2. + (3*complex(0,1)*R13**2*R32*R33*Rdelta3)/2. + (3*complex(0,1)*R12*R13*R33**2*Rdelta3)/2.',
                 order = {'QED':2})

GC_84 = Coupling(name = 'GC_84',
                 value = '-6*complex(0,1)*lam*R13**4 - 3*delta2*complex(0,1)*R13**2*R23**2 - (3*d2*complex(0,1)*R23**4)/2. + 6*complex(0,1)*Idelta3*R13**2*R23*R33 + 6*complex(0,1)*Id1*R23**3*R33 - 3*delta2*complex(0,1)*R13**2*R33**2 - 3*d2*complex(0,1)*R23**2*R33**2 - 6*complex(0,1)*Id1*R23*R33**3 - (3*d2*complex(0,1)*R33**4)/2. - (3*complex(0,1)*R23**4*Rd1)/2. + 9*complex(0,1)*R23**2*R33**2*Rd1 - (3*complex(0,1)*R33**4*Rd1)/2. - (3*complex(0,1)*R23**4*Rd3)/2. + 3*R23**3*R33*Rd3 + 3*R23*R33**3*Rd3 + (3*complex(0,1)*R33**4*Rd3)/2. - 3*complex(0,1)*R13**2*R23**2*Rdelta3 + 3*complex(0,1)*R13**2*R33**2*Rdelta3',
                 order = {'QED':2})

GC_85 = Coupling(name = 'GC_85',
                 value = '(ee**2*complex(0,1))/(2.*sw**2)',
                 order = {'QED':2})

GC_86 = Coupling(name = 'GC_86',
                 value = '-((ee**2*complex(0,1))/sw**2)',
                 order = {'QED':2})

GC_87 = Coupling(name = 'GC_87',
                 value = '(cw**2*ee**2*complex(0,1))/sw**2',
                 order = {'QED':2})

GC_88 = Coupling(name = 'GC_88',
                 value = '(ee**2*complex(0,1)*R11**2)/(2.*sw**2)',
                 order = {'QED':2})

GC_89 = Coupling(name = 'GC_89',
                 value = '(ee**2*complex(0,1)*R11*R12)/(2.*sw**2)',
                 order = {'QED':2})

GC_9 = Coupling(name = 'GC_9',
                value = 'complex(0,1)*G',
                order = {'QCD':1})

GC_90 = Coupling(name = 'GC_90',
                 value = '(ee**2*complex(0,1)*R12**2)/(2.*sw**2)',
                 order = {'QED':2})

GC_91 = Coupling(name = 'GC_91',
                 value = '(ee**2*complex(0,1)*R11*R13)/(2.*sw**2)',
                 order = {'QED':2})

GC_92 = Coupling(name = 'GC_92',
                 value = '(ee**2*complex(0,1)*R12*R13)/(2.*sw**2)',
                 order = {'QED':2})

GC_93 = Coupling(name = 'GC_93',
                 value = '(ee**2*complex(0,1)*R13**2)/(2.*sw**2)',
                 order = {'QED':2})

GC_94 = Coupling(name = 'GC_94',
                 value = '-0.5*(ee*complex(0,1))/sw',
                 order = {'QED':1})

GC_95 = Coupling(name = 'GC_95',
                 value = '(ee*complex(0,1))/(2.*sw)',
                 order = {'QED':1})

GC_96 = Coupling(name = 'GC_96',
                 value = '(ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_97 = Coupling(name = 'GC_97',
                 value = '(CKM1x1*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_98 = Coupling(name = 'GC_98',
                 value = '(CKM1x2*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_99 = Coupling(name = 'GC_99',
                 value = '(CKM1x3*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

