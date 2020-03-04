from flask import Flask, render_template
from models import Model25

application = Flask(__name__)

name = 'RIDHO MARHABAN'
content = 'ini adalah berita baru, akan tetapi berasal dari orang lama'
time = 'jam 11'

@application.route('/')
def index():
	# membuat objek dari kelas Model25
	model = Model25()

	# mengisi nilai ke dalam model
	model.setName('name')
	model.setTitle('Berita terkini!')
	model.setDate('18/08/2019')
	model.setContent(content)
	model.setTime(time)
	model.setDatetime('12/januari/2019, 08:00')

	# mengirimkan nilai ke view
	return render_template('berita.html', judul=model.getTitle(),
		tanggal=model.getDate(),
		isi=model.getContent(),
		waktu=model.getTime(),
		tanggaldanwaktu=model.getDatetime())

if __name__ == '__main__':
	application.run(debug=True)
