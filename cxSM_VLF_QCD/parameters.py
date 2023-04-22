# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 12.3.1 for Microsoft Windows (64-bit) (June 24, 2021)
# Date: Wed 19 Oct 2022 16:38:21



from object_library import all_parameters, Parameter


from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot

# This is a default parameter object representing 0.
ZERO = Parameter(name = 'ZERO',
                 nature = 'internal',
                 type = 'real',
                 value = '0.0',
                 texname = '0')

# This is a default parameter object representing the renormalization scale (MU_R).
MU_R = Parameter(name = 'MU_R',
                 nature = 'external',
                 type = 'real',
                 value = 91.188,
                 texname = '\\text{\\mu_r}',
                 lhablock = 'LOOP',
                 lhacode = [1])

# User-defined parameters.
cabi = Parameter(name = 'cabi',
                 nature = 'external',
                 type = 'real',
                 value = 0.227736,
                 texname = '\\theta _c',
                 lhablock = 'CKMBLOCK',
                 lhacode = [ 1 ])

Rb1 = Parameter(name = 'Rb1',
                nature = 'external',
                type = 'real',
                value = 0.,
                texname = 'b_R',
                lhablock = 'Dependent',
                lhacode = [ 1 ])

Ib1 = Parameter(name = 'Ib1',
                nature = 'external',
                type = 'real',
                value = 0.,
                texname = 'b_i',
                lhablock = 'Dependent',
                lhacode = [ 2 ])

Rd1 = Parameter(name = 'Rd1',
                nature = 'external',
                type = 'real',
                value = 0.,
                texname = 'd_R',
                lhablock = 'Dependent',
                lhacode = [ 3 ])

Id1 = Parameter(name = 'Id1',
                nature = 'external',
                type = 'real',
                value = 0.,
                texname = 'd_i',
                lhablock = 'Dependent',
                lhacode = [ 4 ])

Rdelta1 = Parameter(name = 'Rdelta1',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\delta _R',
                    lhablock = 'Dependent',
                    lhacode = [ 5 ])

Idelta1 = Parameter(name = 'Idelta1',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\delta _i',
                    lhablock = 'Dependent',
                    lhacode = [ 6 ])

d2 = Parameter(name = 'd2',
               nature = 'external',
               type = 'real',
               value = 0.,
               texname = 'd_2',
               lhablock = 'Dependent',
               lhacode = [ 7 ])

theta12 = Parameter(name = 'theta12',
                    nature = 'external',
                    type = 'real',
                    value = 0.73,
                    texname = '\\theta _{12}',
                    lhablock = 'NP',
                    lhacode = [ 1 ])

theta23 = Parameter(name = 'theta23',
                    nature = 'external',
                    type = 'real',
                    value = -0.73,
                    texname = '\\theta _{23}',
                    lhablock = 'NP',
                    lhacode = [ 2 ])

theta13 = Parameter(name = 'theta13',
                    nature = 'external',
                    type = 'real',
                    value = 1.6707963267900001,
                    texname = '\\theta _{13}',
                    lhablock = 'NP',
                    lhacode = [ 3 ])

delta2 = Parameter(name = 'delta2',
                   nature = 'external',
                   type = 'real',
                   value = 0.,
                   texname = '\\delta _2',
                   lhablock = 'NP',
                   lhacode = [ 4 ])

b2 = Parameter(name = 'b2',
               nature = 'external',
               type = 'real',
               value = 0,
               texname = 'b_2',
               lhablock = 'NP',
               lhacode = [ 5 ])

Rc1 = Parameter(name = 'Rc1',
                nature = 'external',
                type = 'real',
                value = 0,
                texname = 'c_R',
                lhablock = 'NP',
                lhacode = [ 6 ])

Ic1 = Parameter(name = 'Ic1',
                nature = 'external',
                type = 'real',
                value = 0,
                texname = 'c_i',
                lhablock = 'NP',
                lhacode = [ 7 ])

Rc2 = Parameter(name = 'Rc2',
                nature = 'external',
                type = 'real',
                value = 0,
                texname = 'c_{2 R}',
                lhablock = 'NP',
                lhacode = [ 8 ])

Ic2 = Parameter(name = 'Ic2',
                nature = 'external',
                type = 'real',
                value = 0,
                texname = 'c_{2 i}',
                lhablock = 'NP',
                lhacode = [ 9 ])

Rdelta3 = Parameter(name = 'Rdelta3',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\delta _{3 R}',
                    lhablock = 'NP',
                    lhacode = [ 10 ])

Idelta3 = Parameter(name = 'Idelta3',
                    nature = 'external',
                    type = 'real',
                    value = -3.5,
                    texname = '\\delta _{3 i}',
                    lhablock = 'NP',
                    lhacode = [ 11 ])

Rd3 = Parameter(name = 'Rd3',
                nature = 'external',
                type = 'real',
                value = 0.,
                texname = 'd_{3 R}',
                lhablock = 'NP',
                lhacode = [ 12 ])

Id3 = Parameter(name = 'Id3',
                nature = 'external',
                type = 'real',
                value = 0.,
                texname = 'd_{3 i}',
                lhablock = 'NP',
                lhacode = [ 13 ])

lamX = Parameter(name = 'lamX',
                 nature = 'external',
                 type = 'real',
                 value = 1.97989,
                 texname = '\\lambda _{\\chi }',
                 lhablock = 'NP',
                 lhacode = [ 14 ])

vs = Parameter(name = 'vs',
               nature = 'external',
               type = 'real',
               value = 200.,
               texname = 'v_s',
               lhablock = 'NP',
               lhacode = [ 15 ])

aEWM1 = Parameter(name = 'aEWM1',
                  nature = 'external',
                  type = 'real',
                  value = 127.9,
                  texname = '\\text{aEWM1}',
                  lhablock = 'SMINPUTS',
                  lhacode = [ 1 ])

Gf = Parameter(name = 'Gf',
               nature = 'external',
               type = 'real',
               value = 0.0000116637,
               texname = 'G_f',
               lhablock = 'SMINPUTS',
               lhacode = [ 2 ])

aS = Parameter(name = 'aS',
               nature = 'external',
               type = 'real',
               value = 0.1184,
               texname = '\\alpha _s',
               lhablock = 'SMINPUTS',
               lhacode = [ 3 ])

ymdo = Parameter(name = 'ymdo',
                 nature = 'external',
                 type = 'real',
                 value = 0.00504,
                 texname = '\\text{ymdo}',
                 lhablock = 'YUKAWA',
                 lhacode = [ 1 ])

ymup = Parameter(name = 'ymup',
                 nature = 'external',
                 type = 'real',
                 value = 0.00255,
                 texname = '\\text{ymup}',
                 lhablock = 'YUKAWA',
                 lhacode = [ 2 ])

yms = Parameter(name = 'yms',
                nature = 'external',
                type = 'real',
                value = 0.101,
                texname = '\\text{yms}',
                lhablock = 'YUKAWA',
                lhacode = [ 3 ])

ymc = Parameter(name = 'ymc',
                nature = 'external',
                type = 'real',
                value = 1.27,
                texname = '\\text{ymc}',
                lhablock = 'YUKAWA',
                lhacode = [ 4 ])

ymb = Parameter(name = 'ymb',
                nature = 'external',
                type = 'real',
                value = 4.7,
                texname = '\\text{ymb}',
                lhablock = 'YUKAWA',
                lhacode = [ 5 ])

ymt = Parameter(name = 'ymt',
                nature = 'external',
                type = 'real',
                value = 172,
                texname = '\\text{ymt}',
                lhablock = 'YUKAWA',
                lhacode = [ 6 ])

yme = Parameter(name = 'yme',
                nature = 'external',
                type = 'real',
                value = 0.000511,
                texname = '\\text{yme}',
                lhablock = 'YUKAWA',
                lhacode = [ 11 ])

ymm = Parameter(name = 'ymm',
                nature = 'external',
                type = 'real',
                value = 0.10566,
                texname = '\\text{ymm}',
                lhablock = 'YUKAWA',
                lhacode = [ 13 ])

ymtau = Parameter(name = 'ymtau',
                  nature = 'external',
                  type = 'real',
                  value = 1.777,
                  texname = '\\text{ymtau}',
                  lhablock = 'YUKAWA',
                  lhacode = [ 15 ])

msq = Parameter(name = 'msq',
                nature = 'external',
                type = 'real',
                value = 0.,
                texname = '\\text{msq}',
                lhablock = 'FRBlock',
                lhacode = [ 1 ])

lam = Parameter(name = 'lam',
                nature = 'external',
                type = 'real',
                value = 0.,
                texname = '\\text{lam}',
                lhablock = 'FRBlock',
                lhacode = [ 2 ])

MZ = Parameter(name = 'MZ',
               nature = 'external',
               type = 'real',
               value = 91.1876,
               texname = '\\text{MZ}',
               lhablock = 'MASS',
               lhacode = [ 23 ])

Me = Parameter(name = 'Me',
               nature = 'external',
               type = 'real',
               value = 0.000511,
               texname = '\\text{Me}',
               lhablock = 'MASS',
               lhacode = [ 11 ])

MMU = Parameter(name = 'MMU',
                nature = 'external',
                type = 'real',
                value = 0.10566,
                texname = '\\text{MMU}',
                lhablock = 'MASS',
                lhacode = [ 13 ])

MTA = Parameter(name = 'MTA',
                nature = 'external',
                type = 'real',
                value = 1.777,
                texname = '\\text{MTA}',
                lhablock = 'MASS',
                lhacode = [ 15 ])

MU = Parameter(name = 'MU',
               nature = 'external',
               type = 'real',
               value = 0.00255,
               texname = 'M',
               lhablock = 'MASS',
               lhacode = [ 2 ])

MC = Parameter(name = 'MC',
               nature = 'external',
               type = 'real',
               value = 1.27,
               texname = '\\text{MC}',
               lhablock = 'MASS',
               lhacode = [ 4 ])

MT = Parameter(name = 'MT',
               nature = 'external',
               type = 'real',
               value = 172,
               texname = '\\text{MT}',
               lhablock = 'MASS',
               lhacode = [ 6 ])

MD = Parameter(name = 'MD',
               nature = 'external',
               type = 'real',
               value = 0.00504,
               texname = '\\text{MD}',
               lhablock = 'MASS',
               lhacode = [ 1 ])

MS = Parameter(name = 'MS',
               nature = 'external',
               type = 'real',
               value = 0.101,
               texname = '\\text{MS}',
               lhablock = 'MASS',
               lhacode = [ 3 ])

MB = Parameter(name = 'MB',
               nature = 'external',
               type = 'real',
               value = 4.7,
               texname = '\\text{MB}',
               lhablock = 'MASS',
               lhacode = [ 5 ])

mh1 = Parameter(name = 'mh1',
                nature = 'external',
                type = 'real',
                value = 125,
                texname = '\\text{mh1}',
                lhablock = 'MASS',
                lhacode = [ 25 ])

mh2 = Parameter(name = 'mh2',
                nature = 'external',
                type = 'real',
                value = 280,
                texname = '\\text{mh2}',
                lhablock = 'MASS',
                lhacode = [ 102 ])

mh3 = Parameter(name = 'mh3',
                nature = 'external',
                type = 'real',
                value = 420,
                texname = '\\text{mh3}',
                lhablock = 'MASS',
                lhacode = [ 103 ])

WZ = Parameter(name = 'WZ',
               nature = 'external',
               type = 'real',
               value = 2.4952,
               texname = '\\text{WZ}',
               lhablock = 'DECAY',
               lhacode = [ 23 ])

WW = Parameter(name = 'WW',
               nature = 'external',
               type = 'real',
               value = 2.085,
               texname = '\\text{WW}',
               lhablock = 'DECAY',
               lhacode = [ 24 ])

WT = Parameter(name = 'WT',
               nature = 'external',
               type = 'real',
               value = 1.50833649,
               texname = '\\text{WT}',
               lhablock = 'DECAY',
               lhacode = [ 6 ])

wh1 = Parameter(name = 'wh1',
                nature = 'external',
                type = 'real',
                value = 0.00407,
                texname = '\\text{wh1}',
                lhablock = 'DECAY',
                lhacode = [ 25 ])

wh2 = Parameter(name = 'wh2',
                nature = 'external',
                type = 'real',
                value = 1.,
                texname = '\\text{wh2}',
                lhablock = 'DECAY',
                lhacode = [ 102 ])

wh3 = Parameter(name = 'wh3',
                nature = 'external',
                type = 'real',
                value = 1.,
                texname = '\\text{wh3}',
                lhablock = 'DECAY',
                lhacode = [ 103 ])

aEW = Parameter(name = 'aEW',
                nature = 'internal',
                type = 'real',
                value = '1/aEWM1',
                texname = '\\alpha _{\\text{EW}}')

G = Parameter(name = 'G',
              nature = 'internal',
              type = 'real',
              value = '2*cmath.sqrt(aS)*cmath.sqrt(cmath.pi)',
              texname = 'G')

CKM1x1 = Parameter(name = 'CKM1x1',
                   nature = 'internal',
                   type = 'complex',
                   value = 'cmath.cos(cabi)',
                   texname = '\\text{CKM1x1}')

CKM1x2 = Parameter(name = 'CKM1x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'cmath.sin(cabi)',
                   texname = '\\text{CKM1x2}')

CKM1x3 = Parameter(name = 'CKM1x3',
                   nature = 'internal',
                   type = 'complex',
                   value = '0',
                   texname = '\\text{CKM1x3}')

CKM2x1 = Parameter(name = 'CKM2x1',
                   nature = 'internal',
                   type = 'complex',
                   value = '-cmath.sin(cabi)',
                   texname = '\\text{CKM2x1}')

CKM2x2 = Parameter(name = 'CKM2x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'cmath.cos(cabi)',
                   texname = '\\text{CKM2x2}')

CKM2x3 = Parameter(name = 'CKM2x3',
                   nature = 'internal',
                   type = 'complex',
                   value = '0',
                   texname = '\\text{CKM2x3}')

CKM3x1 = Parameter(name = 'CKM3x1',
                   nature = 'internal',
                   type = 'complex',
                   value = '0',
                   texname = '\\text{CKM3x1}')

CKM3x2 = Parameter(name = 'CKM3x2',
                   nature = 'internal',
                   type = 'complex',
                   value = '0',
                   texname = '\\text{CKM3x2}')

CKM3x3 = Parameter(name = 'CKM3x3',
                   nature = 'internal',
                   type = 'complex',
                   value = '1',
                   texname = '\\text{CKM3x3}')

R11 = Parameter(name = 'R11',
                nature = 'internal',
                type = 'real',
                value = 'cmath.cos(theta12)*cmath.cos(theta13)',
                texname = 'R_{11}')

R12 = Parameter(name = 'R12',
                nature = 'internal',
                type = 'real',
                value = 'cmath.cos(theta13)*cmath.sin(theta12)',
                texname = 'R_{12}')

R13 = Parameter(name = 'R13',
                nature = 'internal',
                type = 'real',
                value = 'cmath.sin(theta13)',
                texname = 'R_{13}')

R21 = Parameter(name = 'R21',
                nature = 'internal',
                type = 'real',
                value = '-(cmath.cos(theta23)*cmath.sin(theta12)) - cmath.cos(theta12)*cmath.sin(theta13)*cmath.sin(theta23)',
                texname = 'R_{21}')

R22 = Parameter(name = 'R22',
                nature = 'internal',
                type = 'real',
                value = 'cmath.cos(theta12)*cmath.cos(theta23) - cmath.sin(theta12)*cmath.sin(theta13)*cmath.sin(theta23)',
                texname = 'R_{22}')

R23 = Parameter(name = 'R23',
                nature = 'internal',
                type = 'real',
                value = 'cmath.cos(theta13)*cmath.sin(theta23)',
                texname = 'R_{23}')

R31 = Parameter(name = 'R31',
                nature = 'internal',
                type = 'real',
                value = '-(cmath.cos(theta12)*cmath.cos(theta23)*cmath.sin(theta13)) + cmath.sin(theta12)*cmath.sin(theta23)',
                texname = 'R_{31}')

R32 = Parameter(name = 'R32',
                nature = 'internal',
                type = 'real',
                value = '-(cmath.cos(theta23)*cmath.sin(theta12)*cmath.sin(theta13)) - cmath.cos(theta12)*cmath.sin(theta23)',
                texname = 'R_{32}')

R33 = Parameter(name = 'R33',
                nature = 'internal',
                type = 'real',
                value = 'cmath.cos(theta13)*cmath.cos(theta23)',
                texname = 'R_{33}')

MX = Parameter(name = 'MX',
               nature = 'internal',
               type = 'real',
               value = '(lamX*vs)/cmath.sqrt(2)',
               texname = 'M_X')

MW = Parameter(name = 'MW',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(MZ**2/2. + cmath.sqrt(MZ**4/4. - (aEW*cmath.pi*MZ**2)/(Gf*cmath.sqrt(2))))',
               texname = 'M_W')

ee = Parameter(name = 'ee',
               nature = 'internal',
               type = 'real',
               value = '2*cmath.sqrt(aEW)*cmath.sqrt(cmath.pi)',
               texname = 'e')

sw2 = Parameter(name = 'sw2',
                nature = 'internal',
                type = 'real',
                value = '1 - MW**2/MZ**2',
                texname = '\\text{sw2}')

cw = Parameter(name = 'cw',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(1 - sw2)',
               texname = 'c_w')

sw = Parameter(name = 'sw',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(sw2)',
               texname = 's_w')

g1 = Parameter(name = 'g1',
               nature = 'internal',
               type = 'real',
               value = 'ee/cw',
               texname = 'g_1')

gw = Parameter(name = 'gw',
               nature = 'internal',
               type = 'real',
               value = 'ee/sw',
               texname = 'g_w')

vev = Parameter(name = 'vev',
                nature = 'internal',
                type = 'real',
                value = '(2*MW*sw)/ee',
                texname = '\\text{vev}')

yb = Parameter(name = 'yb',
               nature = 'internal',
               type = 'real',
               value = '(ymb*cmath.sqrt(2))/vev',
               texname = '\\text{yb}')

yc = Parameter(name = 'yc',
               nature = 'internal',
               type = 'real',
               value = '(ymc*cmath.sqrt(2))/vev',
               texname = '\\text{yc}')

ydo = Parameter(name = 'ydo',
                nature = 'internal',
                type = 'real',
                value = '(ymdo*cmath.sqrt(2))/vev',
                texname = '\\text{ydo}')

ye = Parameter(name = 'ye',
               nature = 'internal',
               type = 'real',
               value = '(yme*cmath.sqrt(2))/vev',
               texname = '\\text{ye}')

ym = Parameter(name = 'ym',
               nature = 'internal',
               type = 'real',
               value = '(ymm*cmath.sqrt(2))/vev',
               texname = '\\text{ym}')

ys = Parameter(name = 'ys',
               nature = 'internal',
               type = 'real',
               value = '(yms*cmath.sqrt(2))/vev',
               texname = '\\text{ys}')

yt = Parameter(name = 'yt',
               nature = 'internal',
               type = 'real',
               value = '(ymt*cmath.sqrt(2))/vev',
               texname = '\\text{yt}')

ytau = Parameter(name = 'ytau',
                 nature = 'internal',
                 type = 'real',
                 value = '(ymtau*cmath.sqrt(2))/vev',
                 texname = '\\text{ytau}')

yup = Parameter(name = 'yup',
                nature = 'internal',
                type = 'real',
                value = '(ymup*cmath.sqrt(2))/vev',
                texname = '\\text{yup}')

I1a11 = Parameter(name = 'I1a11',
                  nature = 'internal',
                  type = 'complex',
                  value = 'ydo*complexconjugate(CKM1x1)',
                  texname = '\\text{I1a11}')

I1a12 = Parameter(name = 'I1a12',
                  nature = 'internal',
                  type = 'complex',
                  value = 'ydo*complexconjugate(CKM2x1)',
                  texname = '\\text{I1a12}')

I1a13 = Parameter(name = 'I1a13',
                  nature = 'internal',
                  type = 'complex',
                  value = 'ydo*complexconjugate(CKM3x1)',
                  texname = '\\text{I1a13}')

I1a21 = Parameter(name = 'I1a21',
                  nature = 'internal',
                  type = 'complex',
                  value = 'ys*complexconjugate(CKM1x2)',
                  texname = '\\text{I1a21}')

I1a22 = Parameter(name = 'I1a22',
                  nature = 'internal',
                  type = 'complex',
                  value = 'ys*complexconjugate(CKM2x2)',
                  texname = '\\text{I1a22}')

I1a23 = Parameter(name = 'I1a23',
                  nature = 'internal',
                  type = 'complex',
                  value = 'ys*complexconjugate(CKM3x2)',
                  texname = '\\text{I1a23}')

I1a31 = Parameter(name = 'I1a31',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yb*complexconjugate(CKM1x3)',
                  texname = '\\text{I1a31}')

I1a32 = Parameter(name = 'I1a32',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yb*complexconjugate(CKM2x3)',
                  texname = '\\text{I1a32}')

I1a33 = Parameter(name = 'I1a33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yb*complexconjugate(CKM3x3)',
                  texname = '\\text{I1a33}')

I2a11 = Parameter(name = 'I2a11',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yup*complexconjugate(CKM1x1)',
                  texname = '\\text{I2a11}')

I2a12 = Parameter(name = 'I2a12',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yc*complexconjugate(CKM2x1)',
                  texname = '\\text{I2a12}')

I2a13 = Parameter(name = 'I2a13',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yt*complexconjugate(CKM3x1)',
                  texname = '\\text{I2a13}')

I2a21 = Parameter(name = 'I2a21',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yup*complexconjugate(CKM1x2)',
                  texname = '\\text{I2a21}')

I2a22 = Parameter(name = 'I2a22',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yc*complexconjugate(CKM2x2)',
                  texname = '\\text{I2a22}')

I2a23 = Parameter(name = 'I2a23',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yt*complexconjugate(CKM3x2)',
                  texname = '\\text{I2a23}')

I2a31 = Parameter(name = 'I2a31',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yup*complexconjugate(CKM1x3)',
                  texname = '\\text{I2a31}')

I2a32 = Parameter(name = 'I2a32',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yc*complexconjugate(CKM2x3)',
                  texname = '\\text{I2a32}')

I2a33 = Parameter(name = 'I2a33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yt*complexconjugate(CKM3x3)',
                  texname = '\\text{I2a33}')

I3a11 = Parameter(name = 'I3a11',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM1x1*yup',
                  texname = '\\text{I3a11}')

I3a12 = Parameter(name = 'I3a12',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM1x2*yup',
                  texname = '\\text{I3a12}')

I3a13 = Parameter(name = 'I3a13',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM1x3*yup',
                  texname = '\\text{I3a13}')

I3a21 = Parameter(name = 'I3a21',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM2x1*yc',
                  texname = '\\text{I3a21}')

I3a22 = Parameter(name = 'I3a22',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM2x2*yc',
                  texname = '\\text{I3a22}')

I3a23 = Parameter(name = 'I3a23',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM2x3*yc',
                  texname = '\\text{I3a23}')

I3a31 = Parameter(name = 'I3a31',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM3x1*yt',
                  texname = '\\text{I3a31}')

I3a32 = Parameter(name = 'I3a32',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM3x2*yt',
                  texname = '\\text{I3a32}')

I3a33 = Parameter(name = 'I3a33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM3x3*yt',
                  texname = '\\text{I3a33}')

I4a11 = Parameter(name = 'I4a11',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM1x1*ydo',
                  texname = '\\text{I4a11}')

I4a12 = Parameter(name = 'I4a12',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM1x2*ys',
                  texname = '\\text{I4a12}')

I4a13 = Parameter(name = 'I4a13',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM1x3*yb',
                  texname = '\\text{I4a13}')

I4a21 = Parameter(name = 'I4a21',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM2x1*ydo',
                  texname = '\\text{I4a21}')

I4a22 = Parameter(name = 'I4a22',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM2x2*ys',
                  texname = '\\text{I4a22}')

I4a23 = Parameter(name = 'I4a23',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM2x3*yb',
                  texname = '\\text{I4a23}')

I4a31 = Parameter(name = 'I4a31',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM3x1*ydo',
                  texname = '\\text{I4a31}')

I4a32 = Parameter(name = 'I4a32',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM3x2*ys',
                  texname = '\\text{I4a32}')

I4a33 = Parameter(name = 'I4a33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM3x3*yb',
                  texname = '\\text{I4a33}')

