from google.cloud import translate_v2 as translator
language_list = ["Tamil", "Hindi", "French","Spanish", "German", "Chinese"]
gclient = translator.Client()
avl_g_array = gclient.get_languages()
reverse_dict = {v:k for k,v in avl_g_array.items()}
keys = [reverse_dict[lang] for lang in language_list if lang in reverse_dict]
for k in keys
  print(gclient.translate("Hello world", k))
  
