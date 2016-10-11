using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

using MongoDB.Bson;
using MongoDB.Driver;

public partial class art : System.Web.UI.Page
{
    MongoClient client;
    MongoServer server;
    MongoDatabase db;
    MongoCollection collection;

    List<ArticleArt> articleList;
    MongoCursor<ArticleArt> articleCursor;

    protected void Page_Load(object sender, EventArgs e)
    {
        this.dataBaseInitialization();
        this.loadArticleOfType("Art");
    }

    public void loadArticleOfType(String type)
    {
        int maxVersion = 0;
        foreach (ArticleArt article in this.articleList)
        {
            if (article.articleSubject == type)
            {
                if (article.version > maxVersion)
                {
                    maxVersion = article.version;
                }
            }
        }

        foreach (ArticleArt article in this.articleList)
        {
            if (article.articleSubject == type && article.version == maxVersion)
            {
                this.Page.Title = article.articleName;
                mainDiv.InnerHtml = article.articleContent;
            }
        }
    }

    public void dataBaseInitialization()
    {
        this.client = new MongoClient();
        this.server = client.GetServer();
        this.db = server.GetDatabase("articleDataBase");
        this.collection = db.GetCollection<ArticleArt>("Articles");

        this.articleCursor = this.collection.FindAllAs<ArticleArt>();
        articleCursor.SetLimit(5);
        this.articleList = articleCursor.ToList();
    }
}

public class ArticleArt
{
    public ObjectId Id { get; set; }
    public int version { get; set; }
    public String articleName { get; set; }
    public String articleContent { get; set; }
    public bool isProtected { get; set; }
    public String articleSubject { get; set; }
    public ArticleArt(int version, String articlePath, String articleName, String articleSubject, String articleContent, bool isProtected)
    {
        this.version = version;
        this.articleName = articleName;
        this.articleContent = articleContent;
        this.articleSubject = articleSubject;
        this.isProtected = isProtected;
    }
}