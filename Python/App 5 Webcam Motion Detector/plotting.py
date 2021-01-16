from video import df                                                                          #--------------------------------Importing Librabies
from bokeh.plotting import figure, output_file, show                                          #--------------------------------Importing Librabies
from bokeh.models import HoverTool, ColumnDataSource                                          #--------------------------------Importing Librabies


df["Start_String"] = df["Start"].dt.strftime("%Y-%m-%d-%H-%M-%S")                     #--------------------------------Make the date time according to your manner
df["End_String"] = df["End"].dt.strftime("%Y-%m-%d-%H-%M-%S")                         #--------------------------------Make the date time according to your manner


cds = ColumnDataSource(df)                                                      #--------------------------------It connects column data source to DataFrame


p = figure(x_axis_type = 'datetime', height = 250, width = 1000,  title = "Motion Graph")         #--------------------------------It gives figure to the map
p.quad(left = "Start", right = "End", top = 1, bottom = 0, color = "pink", source = cds)          #--------------------------------Quadrant is shape is added to figure
p.yaxis.minor_tick_line_color = None                                                              #--------------------------------Minor Ticks Remover
p.ygrid[0].ticker.desired_num_ticks = 1                                                           #--------------------------------Grid Lines Remover


hover = HoverTool(tooltips = [("Start", "@Start_String"), ("End", "@End_String")])                       #--------------------------------Hover Tool Creater
p.add_tools(hover)                                                                                       #--------------------------------Adding hover tools


output_file("Graph.html")                                                                   #--------------------------------Making of Graph
show(p)
