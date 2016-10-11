using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

using MongoDB.Bson;
using MongoDB.Driver;

public partial class main : System.Web.UI.Page
{
    MongoClient client;
    MongoServer server;
    MongoDatabase db;
    MongoCollection collection;

    List<ArticleMongoObject> articleList;
    MongoCursor<ArticleMongoObject> articleCursor;

    protected void Page_Load(object sender, EventArgs e)
    {
        this.dataBaseInitialization();
        this.loadArticle();
        this.setLinks();
    }

    public void setLinks()
    {
        String User = "X";
        String UserType = "Y";

        if(Session["UserName"] != null)
        {
            User = Session["UserName"].ToString();
            if ( Session["UserRank"].ToString() == "0" )
            {
                UserType = "Registered user rights";
            }
            else
            {
                if (Session["UserRank"].ToString() == "1")
                {
                    UserType = "Editor rights";
                }
                else
                {
                    UserType = "Administrator rights";
                }
            }
        }
        else
        {
            User = "Unregistered";
            UserType = "Visitator rights";
        }

        navigationDiv.InnerHtml = "<ul class='nav nav-tabs'>" +
                                  "<li class='active'><a href='main.aspx'>Home</a></li>" +
                                  "<li><a href='register.aspx'>Register</a></li>" + 
                                  "<li><a href='login.aspx'>Log In</a></li>" +
                                  "<li><a href='article.aspx'>Articles</a></li>" +
                                  "<li><a href='search.aspx'>Search</a></li>" +
                                  "<li><a href='#'>About Us</a></li>" +
                                  "<li><a href='#'>" + User + "</a></li>" +
                                  "<li><a href='#'>" + UserType + "</a></li></ul>";
    }

    public void dataBaseInitialization()
    {
        this.client = new MongoClient();
        this.server = client.GetServer();
        this.db = server.GetDatabase("articleDataBase");
        this.collection = db.GetCollection<ArticleMongoObject>("Articles");

        this.articleCursor = this.collection.FindAllAs<ArticleMongoObject>();
        articleCursor.SetLimit(500);
        this.articleList = articleCursor.ToList();
    }

    public void loadArticle()
    {
        Random rnd = new Random();

        int randomArticleNumber = rnd.Next(0, articleList.Count());

        ArticleMongoObject currentArticle = articleList.ElementAt<ArticleMongoObject>(randomArticleNumber);

        string fullArticleButton = "<br> <a href='article.aspx' class='btn btn-default btn-lg' role='button'> Read Full Article </a>";
        articleDiv.InnerHtml = currentArticle.articleContent + fullArticleButton;

        Session["Article"] = currentArticle.articleName;
        Session["ArticleVersion"] = currentArticle.version;
    }
}

    public class ArticleMongoObject
    {
        public ObjectId Id { get; set; }
        public int version { get; set; }
        public String articleName { get; set; }
        public String articleContent { get; set; }
        public bool isProtected { get; set; }
        public String articleSubject { get; set; }
        public ArticleMongoObject(int version, String articlePath, String articleName, String articleSubject, String articleContent, bool isProtected)
        {
            this.version = version;
            this.articleName = articleName;
            this.articleContent = articleContent;
            this.articleSubject = articleSubject;
            this.isProtected = isProtected;
        }
    }
