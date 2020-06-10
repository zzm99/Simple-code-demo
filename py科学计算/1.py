from tvtk.api import tvtk

s = tvtk.CubeSource(x_length=1.0, y_length=2.0, z_length=3.0)

m = tvtk.PolyDataMapper(input_connection=s.output_port)

a = tvtk.Actor(mapper=m)

r = tvtk.Renderer(background=(0,0,0))

r.add_actor(a)

w = tvtk.RenderWindow(size=(300,300))

w.add_renderer(r)

i = tvtk.RenderWindowInteractor(render_window=w)

i.initialize()

i.start()

