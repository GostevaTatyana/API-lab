import units

def createMyFeature(ag):
	ExtAPI.CreateFeature("MyFeature")

def generateBoxGeometry(feature,fct):
	ExtAPI.Log.WriteMessage("Generating MyFeature...")

	fromUnit, toUnit = ExtAPI.DataModel.CurrentUnitFromQuantityName("Length"), "m"

	Top = units.ConvertUnit(feature.Properties["Top"].Value, fromUnit, toUnit)
	Height = units.ConvertUnit(feature.Properties["Height"].Value, fromUnit, toUnit)
	Shift = units.ConvertUnit(feature.Properties["Shift"].Value, fromUnit, toUnit)
	Width = units.ConvertUnit(feature.Properties["Width"].Value, fromUnit, toUnit)
	Bottom = units.ConvertUnit(feature.Properties["Bottom"].Value, fromUnit, toUnit)
	
	ExtAPI.Log.WriteMessage(Top.ToString())
	ExtAPI.Log.WriteMessage(Height.ToString())	
	ExtAPI.Log.WriteMessage(Shift.ToString())
	ExtAPI.Log.WriteMessage(Width.ToString())
	ExtAPI.Log.WriteMessage(Bottom.ToString())
	
	bodies=[]
	bodies1=[]
	bodies2=[]
	builder = ExtAPI.DataModel.GeometryBuilder
	
	ExtAPI.Log.WriteMessage("Primitives.Sheet.CreatePolygon")
	polygon = builder.Primitives.Sheet.CreatePolygon([0.,0.,0.,Shift,Height,0.,Shift+Top,Height,0.,Bottom,0.,0.])
	polygon1 = polygon.Generate()
	extrude = builder.Operations.CreateExtrudeOperation([0.,0.,1.],Width)
	bodies.Add(extrude.ApplyTo(polygon1)[0])

	box = builder.Primitives.Sheet.CreatePolygon([1.,1.,0.,2.,1.,0.,2.,2.,0.,1.,2.,0.])	
	box1 = box.Generate()
	bodies1.Add(extrude.ApplyTo(box1)[0])
	
	#Subtract1 = builder.Operations.CreateSubtractOperation([polygon1],[box1])
	#bodies.Add(Subtract1.ApplyTo(polygon1))
	Subtract = builder.Operations.CreateSubtractOperation(bodies1)
	bodies2 = Subtract.ApplyTo(bodies)
	feature.Bodies = bodies2
	feature.MaterialType = MaterialTypeEnum.Freeze

	
	return True
