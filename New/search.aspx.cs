using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

using MongoDB.Bson;
using MongoDB.Driver;

public partial class science : System.Web.UI.Page
{
    MongoClient client;
    MongoServer server;
    MongoDatabase db;
    MongoCollection collection;

    List<ArticleSearch> articleList;
    MongoCursor<ArticleSearch> articleCursor;

    int currentArticleVersion;

    protected void Page_Load(object sender, EventArgs e)
    {
        this.dataBaseInitialization();
        this.currentArticleVersion = Int32.Parse(Session["ArticleVersion"].ToString());
    }

    protected void Button1_Click(object sender, EventArgs e)
    {
        String toSearch = String.Format("{0}", Request.Form["searchInput"]);

        int maxVersion = 0;
        foreach (ArticleSearch article in this.articleList)
        {
            if (article.articleName.Contains(toSearch))
            {
                if (article.version > maxVersion)
                {
                    maxVersion = article.version;
                }
            }
        }

        foreach (ArticleSearch article in this.articleList)
        {
            if (article.articleName.Contains(toSearch) && article.version >= currentArticleVersion)
            {
                Session["Article"] = article.articleName;
                Response.Redirect("article.aspx");
            }
        }
    }

    public void dataBaseInitialization()
    {
        this.client = new MongoClient();
        this.server = client.GetServer();
        this.db = server.GetDatabase("articleDataBase");
        this.collection = db.GetCollection<ArticleSearch>("Articles");

        this.articleCursor = this.collection.FindAllAs<ArticleSearch>();
        articleCursor.SetLimit(500);
        this.articleList = articleCursor.ToList();
    }
}

public class ArticleSearch
{
    public ObjectId Id { get; set; }
    public int version { get; set; }
    public String articleName { get; set; }
    public String articleContent { get; set; }
    public bool isProtected { get; set; }
    public String articleSubject { get; set; }
    public ArticleSearch(int version, String articlePath, String articleName, String articleSubject, String articleContent, bool isProtected)
    {
        this.version = version;
        this.articleName = articleName;
        this.articleContent = articleContent;
        this.articleSubject = articleSubject;
        this.isProtected = isProtected;
    }
}