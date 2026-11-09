# Bygger wordpress/jamfor-utbildningar-wpcode.html från index.html. Kör: python3 tools/build-wpcode.py
import re,sys
src=open('./index.html').read()
css=re.search(r'<style>(.*?)</style>',src,re.S).group(1)
body=src[src.index('</style>')+8:src.index('<script>')]
js=re.search(r'<script>(.*?)</script>',src,re.S).group(1)
R='#iths-jamfor'
css=re.sub(r'/\*.*?\*/','',css,flags=re.S)
def blocks(s):
    out=[];i=0
    while i<len(s):
        j=s.find('{',i)
        if j<0: break
        sel=s[i:j].strip();depth=1;k=j+1
        while depth:
            if s[k]=='{':depth+=1
            elif s[k]=='}':depth-=1
            k+=1
        out.append((sel,s[j+1:k-1]));i=k
    return out
def scope(sel):
    parts=[]
    for p in sel.split(','):
        p=p.strip()
        if p in(':root','body'): parts.append(R)
        elif p.startswith('body '): parts.append(R+p[4:])
        elif p.startswith('dialog') or p.startswith('.dlg') : parts.append(R+' '+p)
        else: parts.append(R+' '+p)
    return ', '.join(parts)
def emit(s):
    o=[]
    for sel,b in blocks(s):
        if 'prefers-color-scheme: dark' in sel or 'data-theme' in sel: continue
        if sel.startswith('@media'): o.append(sel+' {\n'+emit(b)+'}\n')
        else: o.append(scope(sel)+' {'+b+'}\n')
    return ''.join(o)
scoped=emit(css)
# Sidan ligger i WordPress: mindre luft upptill, ärv inte temats stilar
scoped=scoped.replace('padding-block: clamp(48px, 8vw, 80px) 120px;','padding-block: 24px 120px;')
scoped=scoped.replace('#iths-jamfor {\n  background: var(--bg);','#iths-jamfor {\n  background: transparent;',1)
guard=f'''
/* Skydd mot temats globala stilar på iths.se */
{R} button, {R} a.btn {{ text-transform: none !important; letter-spacing: normal !important; height: auto !important; min-height: 0 !important; min-width: 0 !important; box-shadow: none !important; float: none !important; line-height: 1.3 !important; white-space: normal !important; }}
{R} h1, {R} h2, {R} h3, {R} h4 {{ text-transform: none !important; }}
{R} ul, {R} ol {{ float: none; width: auto; }}
{R} table {{ margin: 0; width: 100%; }}
{R} th, {R} td {{ border-left: 0; border-right: 0; }}
'''
html=f'''<!-- IT-Högskolan: Jämför utbildningar. Klistra in hela den här snutten i ett HTML-snippet i WPCode. Genererad från index.html i iths-hemsida/jamfor-utbildningar. -->
<style>
{scoped}{guard}</style>
<div id="iths-jamfor">
{body.strip()}
</div>
<script>
(function(){{
{js}
}})();
</script>
'''
open('./wordpress/jamfor-utbildningar-wpcode.html','w').write(html)
print(len(html))
