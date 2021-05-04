
importar  retro

película  =  retro . Película ( 'SonicTheHedgehog-Genesis-GreenHillZone.Act1-000000.bk2' )
película . paso ()

env  =  retro . hacer (
    juego = película . get_game (),
    estado = Ninguno ,
    # bk2s puede contener cualquier botón que se presione, así que permita todo
    use_restricted_actions = retro . Acciones . TODOS ,
    jugadores = película . jugadores ,
)
env . estado_inicial  =  película . get_state ()
env . reiniciar ()

mientras que la  película . paso ():
    env . render ()
    claves  = []
    de  p  en la  gama ( película . jugadores ):
        para  i  en el  rango ( env . num_buttons ):
            teclas . añadir ( película . get_key ( i , p ))
    env . paso ( llaves )