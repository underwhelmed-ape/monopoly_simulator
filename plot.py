import plotly.plotly
plotly.offline.init_notebook_mode(connected=True)
plotly_plot = plotly.offline.iplot
import plotly.figure_factory as ff

v = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40]

z = [[v[10], v[9], v[8], v[7], v[6], v[5], v[4], v[3], v[2], v[1], v[0]],
     [v[11], 0, 0, 0, 0, 0, 0, 0, 0, 0, v[39]],
     [v[12], 0, 0, 0, 0, 0, 0, 0, 0, 0, v[38]],
     [v[13], 0, 0, 0, 0, 0, 0, 0, 0, 0, v[37]],
     [v[14], 0, 0, 0, 0, 0, 0, 0, 0, 0, v[36]],
     [v[15], 0, 0, 0, 0, 0, 0, 0, 0, 0, v[35]],
     [v[16], 0, 0, 0, 0, 0, 0, 0, 0, 0, v[34]],
     [v[17], 0, 0, 0, 0, 0, 0, 0, 0, 0, v[33]],
     [v[18], 0, 0, 0, 0, 0, 0, 0, 0, 0, v[32]],
     [v[19], 0, 0, 0, 0, 0, 0, 0, 0, 0, v[31]],
     [v[20], v[21], v[22], v[23], v[24], v[25], v[26], v[27], v[28], v[29], v[30]]
     ]


space_names = [['Jail', '', '', '', '', '', '', '', '', '', 'Go'],
               ['', '', '', '', '', '', '', '', '', '', ''],
               ['', '', '', '', '', '', '', '', '', '', ''],
               ['', '', '', '', '', '', '', '', '', '', ''],
               ['', '', '', '', '', '', '', '', '', '', ''],
               ['', '', '', '', '', '', '', '', '', '', ''],
               ['', '', '', '', '', '', '', '', '', '', ''],
               ['', '', '', '', '', '', '', '', '', '', ''],
               ['', '', '', '', '', '', '', '', '', '', ''],
               ['', '', '', '', '', '', '', '', '', '', ''],
               ['', '', '', '', '', '', '', '', '', '', 'Free Parking']]
              
    
colorscale=[[0.0, 'rgb(255,255,255)'], [.01, 'rgb(173,216,230)'],
            [.4, 'rgb(100,149,237)'], [.6, 'rgb(65,105,225)'],
            [.8, 'rgb(0,0,205)'],[1.0, 'rgb(25,25,112)']]

fig = ff.create_annotated_heatmap(z, annotation_text=space_names, colorscale=colorscale)
plotly_plot(fig)
