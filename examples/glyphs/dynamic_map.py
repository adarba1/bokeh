from bokeh.plotting import figure
from bokeh.plotting import output_file
from bokeh.plotting import show
from bokeh.models import Range1d
from bokeh.models import ImageSource
from bokeh.models.tiles import stamen_toner, stamen_toner_labels

output_file('dynamic_map.html')

title = 'Dynamic Map: National Land Cover Dataset'
fig = figure(tools='wheel_zoom,pan', title=title)
fig.x_range = Range1d(start=-15473429, end=2108550)
fig.y_range = Range1d(start=-6315661, end=7264686)
fig.background_fill = "black"
fig.axis.visible = False

# National Land Cover Dataset (http://www.mrlc.gov/nlcd2011.php)
service_url = 'http://raster.nationalmap.gov/arcgis/rest/services/LandCover/USGS_EROS_LandCover_NLCD/MapServer/export?'
service_url += 'bbox={XMIN},{YMIN},{XMAX},{YMAX}&bboxSR=102100&size={HEIGHT}%2C{WIDTH}&imageSR=102100&format=png32&transparent=true&f=image'
image_source_options = {}
image_source_options['url'] = service_url
image_source = ImageSource(**image_source_options)

fig.add_tile(stamen_toner)
fig.add_dynamic_image(image_source)
fig.add_tile(stamen_toner_labels, **dict(render_parents=True))

show(fig)
