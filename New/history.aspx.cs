using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

using MongoDB.Bson;
using MongoDB.Driver;

public partial class history : System.Web.UI.Page
{
    MongoClient client;
    MongoServer server;
    MongoDatabase db;
    MongoCollection collection;

    List<ArticleHistory> articleList;
    MongoCursor<ArticleHistory> articleCursor;

    protected void Page_Load(object sender, EventArgs e)
    {
        this.dataBaseInitialization();
        this.loadArticleOfType("History");
    }

    public void loadArticleOfType(String type)
    {
        int maxVersion = 0;
        foreach (ArticleHistory article in this.articleList)
        {
            if (article.articleSubject == type)
            {
                if (article.version > maxVersion)
                {
                    maxVersion = article.version;
                }
            }
        }

        foreach (ArticleHistory article in this.articleList)
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
        this.collection = db.GetCollection<ArticleHistory>("Articles");

        this.articleCursor = this.collection.FindAllAs<ArticleHistory>();
        articleCursor.SetLimit(5);
        this.articleList = articleCursor.ToList();
    }
}

public class ArticleHistory
{
    public ObjectId Id { get; set; }
    public int version { get; set; }
    public String articleName { get; set; }
    public String articleContent { get; set; }
    public bool isProtected { get; set; }
    public String articleSubject { get; set; }
    public ArticleHistory(int version, String articlePath, String articleName, String articleSubject, String articleContent, bool isProtected)
    {
        this.version = version;
        this.articleName = articleName;
        this.articleContent = articleContent;
        this.articleSubject = articleSubject;
        this.isProtected = isProtected;
    }
}