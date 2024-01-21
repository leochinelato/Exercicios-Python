frase = "fui no mercado"

# fatiamento
print(frase[4])
print(frase[4:8])
print(frase[4:14])
print(frase[4:14:2])
print(frase[:5])
print(frase[0:5])
print(frase[8:])
print(frase[9::3])

# analise
print( len(frase) )
print( frase.count('o') )
print( frase.count('o',0,13) )
print( frase.find('fui') )
print( frase.find('Android') )
'mercado' in frase

# transformação
print( frase.replace( "mercado" , "shopping" ) )
print( frase.upper() )
print( frase.lower() )
print( frase.capitalize() )
print( frase.title() )
print( frase.strip() )
print( frase.rstrip() )
print( frase.lstrip() )

# divisão
print( frase.split() )

# junção
print( '-'.join(frase) )

#print com """":
print("""äs dopasd askdakdpadkaodkp aspdk psok 
      paoskdpp oksposak pasodkapso kapso kk k
      asokpsokp asokpd aoskdp aoskadmawmdm fd
      n0fm1309kf woif  wpoefje masd aposdk s""")

#

dividido = frase.split()

print(dividido[0])