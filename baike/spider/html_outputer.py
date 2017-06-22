# coding=utf-8
from json import encoder


class HtmlOutputer(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        # fout = open('output.html', 'w',encoding='utf-8')
        # fout.write("<html>")
        # fout.write("<meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\" /> ")
        # fout.write("<body>")
        # fout.write("<table>")
        # # ascii
        # for data in self.datas:
        #     fout.write("<tr>")
        #     fout.write("<td>%s</td>" % data['url'])
        #     fout.write("<td>%s</td>" % data['title'])
        #     fout.write("<td>%s</td>" % data['summary'])
        # fout.write("</table>")
        # fout.write("</body>")
        # fout.write("</html>")

        fout = open('output.txt', 'w', encoding='utf-8')
        for data in self.datas:
            # fout.write("%s" % data['url'])
            # fout.write("%s" % data['title'])
            # fout.write("%s" % data['summary'])
            fout.write("%s %s %s "% (data['url'],data['title'],data['summary']))
        fout.close()
