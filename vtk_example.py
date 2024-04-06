import vtk

# 读取PLY文件
reader = vtk.vtkPLYReader()
reader.SetFileName("./models/chair.ply")
reader.Update()

# 创建Mapper和Actor
mapper = vtk.vtkPolyDataMapper()
mapper.SetInputConnection(reader.GetOutputPort())

actor = vtk.vtkActor()
actor.SetMapper(mapper)

# 创建渲染器和渲染窗口
renderer = vtk.vtkRenderer()
renderer.AddActor(actor)

renderWindow = vtk.vtkRenderWindow()
renderWindow.AddRenderer(renderer)
renderWindow.SetSize(500, 600)
renderWindow.SetPosition(900, 400)

renderWindowInteractor = vtk.vtkRenderWindowInteractor()
renderWindowInteractor.SetRenderWindow(renderWindow)

# 打开窗口并显示网格模型
renderWindow.Render()
renderWindowInteractor.Start()
