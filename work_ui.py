# __*__ encoding:utf-8 __*__
import wx
import wx.grid
import test

class UI(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self,parent=None,title="成绩查询",size=(900,560))


		grid = wx.grid.Grid(self,pos=(10,0),size=(750,500))
		grid.CreateGrid(20,7)
		for i in range(20):
			for j in range(7):
				grid.SetCellAlignment(i,j,wx.ALIGN_CENTER,wx.ALIGN_CENTER)
		grid.SetColLabelValue(0, "星期一")  #第一列标签
		grid.SetColLabelValue(1, "星期二")
		grid.SetColLabelValue(2, "星期三")
		grid.SetColLabelValue(3, "星期四")
		grid.SetColLabelValue(4, "星期五")  # 第一列标签
		grid.SetColLabelValue(5, "星期六")
		grid.SetColLabelValue(6, "星期日")

		grid.SetColSize(0,100)
		grid.SetColSize(1,100)
		grid.SetColSize(2,100)
		grid.SetColSize(3,100)
		grid.SetColSize(4,100)
		grid.SetColSize(5,100)
		grid.SetColSize(6,100)
		grid.SetRowSize(0, 90)
		grid.SetRowSize(1, 90)
		grid.SetRowSize(2, 90)
		grid.SetRowSize(3, 90)
		grid.SetRowSize(4, 90)

		grid.SetCellTextColour("NAVY")

		data = test.search()
		for i in range(5):
			for j in range(7):
				file_handle = open('txt/%s.txt'%(i*7+j), mode='w', encoding='utf8')
				grid.SetCellValue(i, j, data[i*7+j])
				file_handle.writelines(data[i*7+j]+"\n")
				file_handle.close()


		pass


app = wx.App()
frame = UI()
frame.Show()
app.MainLoop()
