import 'package:flutter/material.dart';
import 'http_model.dart';
import 'http_service.dart';
import 'package:http/http.dart' as http;

class PostsPage extends StatelessWidget {
  final HttpService httpService = HttpService();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("Posts"),
      ),
      body: FutureBuilder(
        future: httpService.getPosts(),
        builder: (BuildContext context, AsyncSnapshot<List<Post>> snapshot) {
          if (snapshot.hasData) {
            List<Post> posts = snapshot.data;
            return ListView(
              children: posts
                  .map(
                    (Post post) => ListTile(
                      title: Text(post.user),
                      subtitle: Text(post.body),
                    ),
                  )
                  .toList(),
            );
          } else {
            print("waiting2");
            return Center(child: CircularProgressIndicator());
          }
        },
      ),
    );
  }
}
