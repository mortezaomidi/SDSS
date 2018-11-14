"""Tools are added to a .pyt as classes.
 Each tool class should include at a minimum
 an __init__ and execute method. Optionally,
 getParameterInfo, isLicensed, updateParameters,
 and updateMessages methods can be used to add
 additional control to the behavior of the tool."""


import arcpy


class Toolbox(object):
    def __init__(self):
        """SDSS for ... ."""
        self.label = "SDSS-Tools"
        self.alias = "SDSS for..."

        # List of tool classes associated with this toolbox
        self.tools = [Download,]

# List of tool classes associated with this toolbox
class Download(object):
    def __init__(self):
        """This tool is used for download landsat data."""
        self.label = "Download Landsat data"
        self.description = "This tool is used for downloading landsat data."
        self.canRunInBackground = False
		# self.category = "Base_Tools"
		# self.stylesheet = To change the default stylesheet used for the tool.
		
	#Define parameter definitions
    def getParameterInfo(self):		
		# Input Features parameter
		
		# First parameter
		param0 = arcpy.Parameter(
			displayName = "Search from:",
			name = "in_start_date",
			datatype = "GPDate",
			parameterType = "Required",
			direction = "Input")
		
		param0.value = r"11/15/2018"
			
		
		# Second parameter
		param1 = arcpy.Parameter(
			displayName = "Search to:",
			name = "in_to_date",
			datatype = "GPDate",
			parameterType = "Required",
			direction = "Input")
			
		param1.value = "11/15/2019"
		
		# Third parameter
		months_name = ['mehr', 'aban', 'azar']
		param2 = arcpy.Parameter(
			displayName = "Search months:",
			name = "in_search_months",
			datatype = "GPString",
			parameterType = "Required",
			direction = "Input")
		
		param2.value = months_name[0]
		
		# Fourth parameter
		param3 = arcpy.Parameter(
			displayName = "Study Area:",
			name = "in_study_area",
			datatype = "GPFeatureLayer",
			parameterType = "Required",
			direction = "Input")
			
		# Fifth parameter
		param4 = arcpy.Parameter(
			displayName = "Output Dir:",
			name = "out_dir",
			datatype = "Feature Set",
			parameterType = "Required",
			direction = "Output")
			
		# Set  acceptable data for inputs		
		param2.filter.type = "ValueList"		
		param2.filter.list = months_name
		param3.filter.list = ["Polygon"]
		# param5.parameterDependencies = [param1.name]
		# param2.schema.clone = True
		
		# Use __file__ attribute to find the .lyr file (assuming the
		#  .pyt and .lyr files exist in the same folder).
		#param1.symbology = os.path.join(os.path.dirname(__file__), 
										#'raster_symbology.lyr')										
        
		params = [param0, param1, param2, param3, param4]
		
		return params
		

    def isLicensed(self):        
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""
        return
