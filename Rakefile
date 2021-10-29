task :notify => ["notify:pingomatic", "notify:google", "notify:bing"]
desc "Notify various services that the site has been updated"
namespace :notify do
  desc "Notify Ping-O-Matic"
  task :pingomatic do
    begin
      require "xmlrpc/client"
      puts "* Notifying Ping-O-Matic that the site has updated"
      XMLRPC::Client.new("rpc.pingomatic.com", "/").call("weblogUpdates.extendedPing", "neontapir.github.io", "//neontapir.github.io", "//neontapir.github.io/atom.xml", "//neontapir.github.io/feed.xml")
    rescue LoadError
      puts "! Could not ping ping-o-matic, because XMLRPC::Client could not be found."
    end
  end

  desc "Notify Google of updated sitemap"
  task :google do
    begin
      require "net/http"
      require "uri"
      puts "* Notifying Google that the site has updated"
      Net::HTTP.get("www.google.com", "/webmasters/tools/ping?sitemap=" + URI.escape("//neontapir.github.io/sitemap.xml"))
    rescue LoadError
      puts "! Could not ping Google about our sitemap, because Net::HTTP or URI could not be found."
    end
  end

  desc "Notify Bing of updated sitemap"
  task :bing do
    begin
      require "net/http"
      require "uri"
      puts "* Notifying Bing that the site has updated"
      Net::HTTP.get("www.bing.com", "/webmaster/ping.aspx?siteMap=" + URI.escape("//neontapir.github.io/sitemap.xml"))
    rescue LoadError
      puts "! Could not ping Bing about our sitemap, because Net::HTTP or URI could not be found."
    end
  end
end

PORT = 4001

desc "Serve"
task :serve do
  sh %Q[bundle exec jekyll serve --port #{PORT} --incremental]
end

desc "Serve without incremental"
task :serve_all do
  sh %Q[bundle exec jekyll serve --port #{PORT}]
end

desc "Profile Liquid"
task :profile do
  sh %Q[bundle exec jekyll build --profile]
end

desc "Default is to build everything"
task :default => :serve
