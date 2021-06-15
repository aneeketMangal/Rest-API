import 'dart:convert';
import 'package:http/http.dart' as http;
import 'package:http/http.dart';

import 'http_model.dart';

class HttpService {
  final String postsURL =
      "https://aneeket.pythonanywhere.com/recieve?name=tempUser";

  Future<List<Post>> getPosts() async {
    final uri = Uri.parse(postsURL);
    print(uri);
    http.Response res = await http.get(uri);
    print("trying");
    print(res.statusCode);

    if (res.statusCode == 200) {
      List<dynamic> body = jsonDecode(res.body);
      print(body);

      List<Post> posts = body
          .map(
            (dynamic item) => Post.fromJson(item),
          )
          .toList();
      print("yahan tak ok");
      return posts;
    } else {
      print("fdsa");
      throw "Unable to retrieve posts.";
    }
  }
}
