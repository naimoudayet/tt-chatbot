import 'dart:convert';

import 'package:chatbot_mobile/config/api.dart';
import 'package:chatbot_mobile/consts/colors.dart';
import 'package:chatbot_mobile/models/user_model.dart';
import 'package:chatbot_mobile/screens/home_page.dart';
import 'package:chatbot_mobile/screens/inscription_page.dart';
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'package:toast/toast.dart';
import 'package:shared_preferences/shared_preferences.dart';

class LoginPage extends StatefulWidget {
  const LoginPage({super.key});

  @override
  State<LoginPage> createState() => _LoginPageState();
}

class _LoginPageState extends State<LoginPage> {
  final TextEditingController _emailController = TextEditingController();
  final TextEditingController _passwordController = TextEditingController();

  @override
  void initState() {
    super.initState();

    _emailController.text = "client@gmail.com";
    _passwordController.text = "client";
  }

  Future<void> _login() async {
    final String email = _emailController.text;
    final String password = _passwordController.text;

    if (email.isEmpty) {
      // message erreur
      Toast.show("Email champs obligatoire",
          duration: Toast.lengthLong, gravity: Toast.bottom);
    } else if (password.isEmpty) {
      // message erreur
      Toast.show("Mot de passe champs obligatoire",
          duration: Toast.lengthLong, gravity: Toast.bottom);
    } else {
      // Make HTTP request to login endpoint
      final Uri url = Uri.parse(loginUrl);
      final headers = {'Content-Type': 'application/json'};
      final body = jsonEncode({
        'email': email,
        'password': password,
      });

      final response = await http.post(url, body: body, headers: headers);

      debugPrint("Status code: ${response.statusCode}");
      if (response.statusCode == 200) {
        final data = jsonDecode(response.body);
        UserModel user = UserModel.fromJson(data['user']);

        SharedPreferences prefs = await SharedPreferences.getInstance();
        await prefs.setBool("CONNECTED", true);
        await prefs.setString("USER_ID", user.id!);
        await prefs.setString("ROLE", user.role!);
        // redirect homepage
        Navigator.pushReplacement(
            context, MaterialPageRoute(builder: (context) => const HomePage()));
      } else if (response.statusCode == 401) {
        Toast.show("svp, vérifier votre email et mot de passe",
            duration: Toast.lengthLong, gravity: Toast.bottom);
      } else {
        Toast.show("Erreur", duration: Toast.lengthLong, gravity: Toast.bottom);
      }
    }
  }

  @override
  Widget build(BuildContext context) {
    ToastContext().init(context);

    return Scaffold(
      backgroundColor: Colors.white,
      appBar: AppBar(
        backgroundColor: primaryColor,
        elevation: 10,
        title: const Text(
          "Authentification",
          style: TextStyle(color: Colors.white),
        ),
      ),
      body: SingleChildScrollView(
        child: Padding(
          padding: const EdgeInsets.all(16.0),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.stretch,
            children: [
              const SizedBox(height: 20),
              Center(
                child: Image.asset(
                  'assets/images/logo.png', // Replace with your image asset
                  height: 150,
                ),
              ),
              const SizedBox(height: 40),
              TextField(
                controller: _emailController,
                decoration: const InputDecoration(
                  labelText: 'Email',
                  border: OutlineInputBorder(),
                ),
                keyboardType: TextInputType.emailAddress,
              ),
              const SizedBox(height: 20),
              TextField(
                controller: _passwordController,
                decoration: const InputDecoration(
                  labelText: 'Password',
                  border: OutlineInputBorder(),
                ),
                obscureText: true,
              ),
              const SizedBox(height: 40),
              ElevatedButton(
                onPressed: _login,
                style: ElevatedButton.styleFrom(
                  backgroundColor: primaryColor,
                ),
                child: const Text(
                  'Se Connecter',
                  style: TextStyle(color: Colors.white),
                ),
              ),
              const SizedBox(height: 20),
              Center(
                child: GestureDetector(
                  onTap: () {
                    Navigator.push(
                      context,
                      MaterialPageRoute(
                          builder: (context) => const InscriptionPage()),
                    );
                  },
                  child: const Text(
                    "Vous n'avez pas de compte ? S'inscrire",
                    style: TextStyle(color: primaryColor),
                  ),
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
