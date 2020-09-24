from flask import Flask, render_template, url_for
app = Flask(__name__)


posts = [
    {
        "author":"Stephany Spencer",
        "title": "There and Back Again : Scaling Multi Tenant Kubernetes Clusters",
        "content":"They say there are lessons to be learned in IT 'war stories'. But maybe the real lessons are what happened afterwards, not the event or even what led up to the event? Just as the event is not the whole story, nor is any particular tool the whole story.",
        "category":"World",
        "date_posted":"April 20, 2020"

    },
    {
        "author":"Nimay Parekh",
        "title":"Inside Product: Introduction to Feature Priority using ICE (Impact, Confidence, Ease) and GIST (Goals, Ideas, Step-Projects and Tasks)",
        "content":"When considering product rollouts, there are literally a dozen frameworks that one can consider when isolating priority within qualitative and quantitative data. Frameworks vary by stage of business, product type, customer type, willingness to pay and accessibility to data. Coined and popularized by Sean Ellis, the ICE framework may be the most popular useful framework when scaling and optimizing on shipping time, developer ROI, user retention and funnel maximization.",
        "category":"Design",
        "date_posted":"April 20, 2020"

    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html", posts=posts, title="bb")

@app.route('/about')
def about():
    return render_template("home.html")



if __name__ == "__main__":
    app.run(debug=True)