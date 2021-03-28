# Import points from a text file
import rhinoscriptsyntax as rs

def ImportPoints():
    #prompt the user for a file to import
    filter = "Text file (*.txt)|*.txt|All Files (*.*)|*.*||"
    filename = rs.OpenFileName("Open Point File", filter)
    if not filename: return

    #read each line from the file
    file = open(filename, "r")
    contents = file.readlines()
    file.close()

    # local helper function    
    def __point_from_string(text):
        items = text.strip("()\n").split(",")
        center_x = float(items[0])
        center_y = float(items[1])
        r = float(items[2])
        return center_x, center_y, r

    for entry in contents:
        if entry != "&\n":
            info = __point_from_string(entry)
            center = (info[0], info[1])
            radius = info[2]
            rs.AddSphere(center, radius)


##########################################################################
# Check to see if this file is being executed as the "main" python
# script instead of being used as a module by some other python script
# This allows us to use the module which ever way we want.
if( __name__ == "__main__" ):
    ImportPoints()