# Genera index.html a partir de index.src.html insertando el símbolo del logo
import re
sym = open('assets/logo-symbol.svg.txt', encoding='utf-8').read()
vb = re.search(r'viewBox="([^"]+)"', sym).group(1)
src = open('index.src.html', encoding='utf-8').read()
open('index.html', 'w', encoding='utf-8').write(src.replace('{{LOGO_SYMBOL}}', sym).replace('{{LOGO_VB}}', vb))
print('index.html generado')
