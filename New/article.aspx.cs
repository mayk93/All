using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

using MongoDB.Bson;
using MongoDB.Driver;

public partial class article : System.Web.UI.Page
{
    MongoClient client;
    MongoServer server;
    MongoDatabase db;
    MongoCollection collection;

    List<Article> articleList;
    MongoCursor<Article> articleCursor;

    int currentArticleVersion;

    protected void Page_Load(object sender, EventArgs e)
    {
        dataBaseInitialization();

        String nameOfArticleToLoad = Session["Article"].ToString();
        this.currentArticleVersion = Int32.Parse(Session["ArticleVersion"].ToString());

        this.Page.Title = nameOfArticleToLoad;

        loadArticle(nameOfArticleToLoad);
    }

    public void loadArticle(String toLoad)
    {
        int maxVersion = 0;
        foreach (Article article in this.articleList)
        {
            if(article.articleName == toLoad)
            {
                if(article.version > maxVersion)
                {
                    maxVersion = article.version;
                }
            }
        }

        foreach (Article article in this.articleList)
        {
            if (article.articleName == toLoad && article.version == currentArticleVersion)
            {
                this.Page.Title = article.articleName;
                mainDiv.InnerHtml = article.articleContent;
                categoryDiv.InnerHtml = categoryDiv.InnerHtml + article.articleSubject;

                Session["Article"] = article.articleName;
                Session["ArticleVersion"] = article.version;
            }
        }
    }

    public void dataBaseInitialization()
    {
        this.client = new MongoClient();
        this.server = client.GetServer();
        this.db = server.GetDatabase("articleDataBase");
        this.collection = db.GetCollection<Article>("Articles");

        this.articleCursor = this.collection.FindAllAs<Article>();
        articleCursor.SetLimit(500);
        this.articleList = articleCursor.ToList();
    }
}

public class Article
{
    public ObjectId Id { get; set; }
    public int version { get; set; }
    public String articleName { get; set; }
    public String articleContent { get; set; }
    public bool isProtected { get; set; }
    public String articleSubject { get; set; }
    public Article(int version, String articlePath, String articleName, String articleSubject, String articleContent, bool isProtected)
    {
        this.version = version;
        this.articleName = articleName;
        this.articleContent = articleContent;
        this.articleSubject = articleSubject;
        this.isProtected = isProtected;
    }
}