Ok, nessa pasta nós temos 2 scripts, o concat.py que será transformado no executável
e o segundo Setup.py, este é resposável pela tranformação, nele, todas as informações 
de biblioteca, includes e excludes devem estar configuradas, reza a lenda que altomaticamente
o cx_freeze(ferramenta ultizada para a conversão) reconhece todas as bibliotecas, mas não vamos acreditar
nisso e evitar dor decabeça.
---------------------------------------
OBS: antes de realizar o comando, certificar-se de estar no diretorio do setup.py e o script a ser convertido usando
o comando cd no terminal.

Após realizarmos a conversão, ultilzando o comando a seguir no terminal teremos a pasta build
onde teremos nosso executável.
	
	python concat.py build -f
