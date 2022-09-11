from flask import Flask, render_template, jsonify,request
import smtplib

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Bengaluru, India',
    'salary': 'Rs 10,00,000',
    'minimum-qualifications-1':'Bachelors Degree in Mathematics, Computer Science or in a similar field.',
    'minimum-qualifications-2': 'Proven working experience as a Data Analyst or Business Data Analyst.',
     'minimum-qualifications-3': 'Technical expertise regarding data models, database design development, data mining and segmentation techniques.',
    'preffered-qualifications-1':'Knowledge of statistics and experience using statistical packages for analyzing datasets (Excel, SPSS, SAS etc)',
     'preffered-qualifications-2':'Strong analytical skills with the ability to collect, organize, analyze, and disseminate significant amounts of information with attention to detail and accuracy',
     'preffered-qualifications-3':'Adept at queries, report writing and presenting findings',
     'preffered-qualifications-4':'Strong knowledge of and experience with reporting packages (Business Objects etc), databases (SQL etc), programming (XML, Javascript, or ETL frameworks)',
    'about-the-job':'We are looking for a passionate certified Data Analyst. The successful candidate will turn data into information, information into insight and insight into business decisions. Data analyst responsibilities include conducting full lifecycle analysis to include requirements, activities and design. Data analysts will develop analysis and reporting capabilities. They will also monitor performance and quality control plans to identify improvements.',
    'responsibilities-1':'Interpret data, analyze results using statistical techniques and provide ongoing reports',
    'responsibilities-2':'Develop and implement databases, data collection systems, data analytics and other strategies that optimize statistical efficiency and quality'
    
  },

  {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Delhi, India',
    'salary': 'Rs 12,00,000',
    'minimum-qualifications-1':'BSc/BA in Computer Science, Engineering or relevant field; graduate degree in Data Science or other quantitative field is preferred',
    'minimum-qualifications-2':'Excellent communication and presentation skills',
    'minimum-qualifications-3':'Problem-solving aptitude',
    'preffered-qualifications-1':'Knowledge of R, SQL and Python; familiarity with Scala, Java or C++ is an asset',
    'preffered-qualifications-2':'Experience using business intelligence tools (e.g. Tableau) and data frameworks (e.g. Hadoop)',
    'preffered-qualifications-3':'Analytical mind and business acumen',
    'preffered-qualifications-4':'Understanding of machine-learning and operations research',
    'about-the-job':'We are looking for a Data Scientist to analyze large amounts of raw information to find patterns that will help improve our company. We will rely on you to build data products to extract valuable business insights.In this role, you should be highly analytical with a knack for analysis, math and statistics. Critical thinking and problem-solving skills are essential for interpreting data. We also want to see a passion for machine-learning and research. Your goal will be to help our company analyze trends to make better decisions.',
    'responsibilities-1':'Identify valuable data sources and automate collection processes',
    'responsibilities-2':'Undertake preprocessing of structured and unstructured data'
  },

  {
    'id': 3,
    'title': 'Frontend Engineer',
    'location': 'Remote',
    'salary': '$100,000',
     'minimum-qualifications-1':'BSc degree in Computer Science or relevant field',
    'minimum-qualifications-2':'Familiarity with software like Adobe Suite, Photoshop and content management systems',
    'minimum-qualifications-3':'An ability to perform well in a fast-paced environment',
    'preffered-qualifications-1':'Proven work experience as a Front-end developer',
    'preffered-qualifications-2':'Hands on experience with markup languages',
    'preffered-qualifications-3':'Experience with JavaScript, CSS and jQuery',
    'preffered-qualifications-4':'In-depth understanding of the entire web development process (design, development and deployment)',
    'about-the-job':'We are looking for a qualified Front-end developer to join our IT team. You will be responsible for building the ‘client-side’ of our web applications. You should be able to translate our company and customer needs into functional and appealing interactive applications. If you’re interested in creating a user-friendly environment by writing code and moving forward in your career, then this job is for you. We expect you to be a tech-savvy professional, who is curious about new digital technologies and aspires to combine usability with visual design. Ultimately, you should be able to create a functional and attractive digital environment for our company, ensuring great user experience.',
    'responsibilities-1':'Use markup languages like HTML to create user-friendly web pages',
    'responsibilities-2':'Maintain and improve website'
  
  },

  {
    'id': 4,
    'title': 'Backend Engineer',
    'location': 'San Francisco, USA',
    'salary': '$120,000',
     'minimum-qualifications-1':'BSc degree in Computer Science or relevant field',
    'minimum-qualifications-2':'Familiarity with front-end languages (e.g. HTML, JavaScript and CSS)',
    'minimum-qualifications-3':'Teamwork skills with a problem-solving attitude',
    'preffered-qualifications-1':'Proven work experience as a Back-end developer',
    'preffered-qualifications-2':'In-depth understanding of the entire web development process (design, development and deployment)',
    'preffered-qualifications-3':'Hands on experience with programming languages like Java, Ruby, PHP and Python',
    'preffered-qualifications-4':'Working knowledge of CMS framework',
    'about-the-job':'We are looking for an experienced Back-end developer to join our IT team. You will be responsible for the server side of our web applications. If you have excellent programming skills and a passion for developing applications or improving existing ones, we would like to meet you. As a Back-end developer, you’ll work closely with our engineers to ensure system consistency and improve user experience. Ultimately, you should be able to develop and maintain functional and stable web applications to meet our company’s needs.',
    'responsibilities-1':'Participate in the entire application lifecycle, focusing on coding and debugging',
    'responsibilities-2':'Write clean code to develop functional web applications'
  }
]

@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS, companyname='Jovian')


@app.route("/apply", methods=["POST"])
def test():
  id = request.form.get("id")
  success = request.form.get("success")
  for job in JOBS:
    id = request.form.get("id")
    if(job['id'] == int(id)):
        title = job['title']
        salary = job['salary']
        location = job['location']
        minimum_qualifications_a = job['minimum-qualifications-1']
        minimum_qualifications_b = job['minimum-qualifications-2']
        minimum_qualifications_c = job['minimum-qualifications-3']
        preffered_qualifications_1 = job['preffered-qualifications-1']
        preffered_qualifications_2 = job['preffered-qualifications-2']
        preffered_qualifications_3 = job['preffered-qualifications-3']
        preffered_qualifications_4 = job['preffered-qualifications-4']
        about_the_job = job['about-the-job']
        responsibilities_1 = job['responsibilities-1']
        responsibilities_2 = job['responsibilities-2']

      
  return render_template('apply.html',jobs=JOBS, id=id,title=title, salary=salary, location=location,minimum_qualifications_1=minimum_qualifications_a,minimum_qualifications_2=minimum_qualifications_b,minimum_qualifications_3=minimum_qualifications_c,preffered_qualifications_1=preffered_qualifications_1,preffered_qualifications_2=preffered_qualifications_2,preffered_qualifications_3=preffered_qualifications_3,preffered_qualifications_4=preffered_qualifications_4,about_the_job=about_the_job,responsibilities_1=responsibilities_1,responsibilities_2=responsibilities_2,success=success)


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


@app.route("/contact")
def contact():
  
  return render_template('contact.html', companyname='Jovian')

@app.route("/success", methods=["POST"])
def success():
  
  return render_template('success.html', companyname='Jovian')


if __name__ == '__main__':
  app.run(host='0.0.0.0',debug=True)