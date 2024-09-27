import funcion_examen as fun
notas=[]
while True:
    fun.menu()
    fun.add_nota(notas)
    fun.del_notas(notas)
    fun.mod_nota(notas)
    fun.calc_notas(notas)
    fun.nota_maxi_minim(notas)
    fun.mostrar_notas(notas)

    break

print("-----\n",notas)