2022-11-13 14:18:14.265327: W tensorflow/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'cudart64_110.dll'; dlerror: cudart64_110.dll not found
2022-11-13 14:18:14.265928: I tensorflow/stream_executor/cuda/cudart_stub.cc:29] Ignore above cudart dlerror if you do not have a GPU set up on your machine.

2022-11-13 14:18:28.582646: W tensorflow/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'nvcuda.dll'; dlerror: nvcuda.dll not found
2022-11-13 14:18:28.583491: W tensorflow/stream_executor/cuda/cuda_driver.cc:263] failed call to cuInit: UNKNOWN ERROR (303)
2022-11-13 14:18:28.594651: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:169] retrieving CUDA diagnostic information for host: MURALI-02
2022-11-13 14:18:28.595008: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:176] hostname: MURALI-02
2022-11-13 14:18:28.600614: I tensorflow/core/platform/cpu_feature_guard.cc:193] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  AVX AVX2
To enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.
Loaded model from disk
 * Serving Flask app "nutrition_analyzer" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
127.0.0.1 - - [13/Nov/2022 14:18:56] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [13/Nov/2022 14:18:57] "GET /static/css/main.css HTTP/1.1" 304 -
127.0.0.1 - - [13/Nov/2022 14:19:00] "GET /favicon.ico HTTP/1.1" 404 -
127.0.0.1 - - [13/Nov/2022 14:19:00] "GET /image1 HTTP/1.1" 200 -
127.0.0.1 - - [13/Nov/2022 14:19:00] "GET /static/js/main.js HTTP/1.1" 304 -
1/1 [==============================] - 1s 568ms/step
prediction [4]
WATERMELON
127.0.0.1 - - [13/Nov/2022 14:19:27] "POST /predict HTTP/1.1" 200 -
127.0.0.1 - - [13/Nov/2022 14:19:27] "GET /static/style.css HTTP/1.1" 404 -
{"items": [{"sugar_g": 6.2, "fiber_g": 0.4, "serving_size_g": 100.0, "sodium_mg": 0, "name": "watermelon", "potassium_mg": 10, "fat_saturated_g": 0.0, "fat_total_g": 0.1, "calories": 30.3, "cholesterol_mg": 0, "protein_g": 0.6, "carbohydrates_total_g": 7.4}]}
[{'sugar_g': 6.2, 'fiber_g': 0.4, 'serving_size_g': 100.0, 'sodium_mg': 0, 'name': 'watermelon', 'potassium_mg': 10, 'fat_saturated_g': 0.0, 'fat_total_g': 0.1, 'calories': 30.3, 'cholesterol_mg': 0, 'protein_g': 0.6, 'carbohydrates_total_g': 7.4}]
1/1 [==============================] - 0s 46ms/step
prediction [1]
BANANA
127.0.0.1 - - [13/Nov/2022 14:20:00] "POST /predict HTTP/1.1" 200 -
127.0.0.1 - - [13/Nov/2022 14:20:00] "GET /static/style.css HTTP/1.1" 404 -
{"items": [{"sugar_g": 12.3, "fiber_g": 2.6, "serving_size_g": 100.0, "sodium_mg": 1, "name": "banana", "potassium_mg": 22, "fat_saturated_g": 0.1, "fat_total_g": 0.3, "calories": 89.4, "cholesterol_mg": 0, "protein_g": 1.1, "carbohydrates_total_g": 23.2}]}
[{'sugar_g': 12.3, 'fiber_g': 2.6, 'serving_size_g': 100.0, 'sodium_mg': 1, 'name': 'banana', 'potassium_mg': 22, 'fat_saturated_g': 0.1, 'fat_total_g': 0.3, 'calories': 89.4, 'cholesterol_mg': 0, 'protein_g': 1.1, 'carbohydrates_total_g': 23.2}]
1/1 [==============================] - 0s 48ms/step
prediction [1]
BANANA
127.0.0.1 - - [13/Nov/2022 14:23:37] "POST /predict HTTP/1.1" 200 -
127.0.0.1 - - [13/Nov/2022 14:23:37] "GET /static/style.css HTTP/1.1" 404 -
{"items": [{"sugar_g": 12.3, "fiber_g": 2.6, "serving_size_g": 100.0, "sodium_mg": 1, "name": "banana", "potassium_mg": 22, "fat_saturated_g": 0.1, "fat_total_g": 0.3, "calories": 89.4, "cholesterol_mg": 0, "protein_g": 1.1, "carbohydrates_total_g": 23.2}]}
[{'sugar_g': 12.3, 'fiber_g': 2.6, 'serving_size_g': 100.0, 'sodium_mg': 1, 'name': 'banana', 'potassium_mg': 22, 'fat_saturated_g': 0.1, 'fat_total_g': 0.3, 'calories': 89.4, 'cholesterol_mg': 0, 'protein_g': 1.1, 'carbohydrates_total_g': 23.2}]
1/1 [==============================] - 0s 62ms/step
prediction [3]
PINEAPPLE
127.0.0.1 - - [13/Nov/2022 14:25:31] "POST /predict HTTP/1.1" 200 -
127.0.0.1 - - [13/Nov/2022 14:25:31] "GET /static/style.css HTTP/1.1" 404 -
{"items": [{"sugar_g": 9.9, "fiber_g": 1.4, "serving_size_g": 100.0, "sodium_mg": 0, "name": "pineapple", "potassium_mg": 8, "fat_saturated_g": 0.0, "fat_total_g": 0.1, "calories": 50.8, "cholesterol_mg": 0, "protein_g": 0.5, "carbohydrates_total_g": 13.0}]}
[{'sugar_g': 9.9, 'fiber_g': 1.4, 'serving_size_g': 100.0, 'sodium_mg': 0, 'name': 'pineapple', 'potassium_mg': 8, 'fat_saturated_g': 0.0, 'fat_total_g': 0.1, 'calories': 50.8, 'cholesterol_mg': 0, 'protein_g': 0.5, 'carbohydrates_total_g': 13.0}]
1/1 [==============================] - 0s 48ms/step
prediction [1]
BANANA
127.0.0.1 - - [13/Nov/2022 14:26:44] "POST /predict HTTP/1.1" 200 -
127.0.0.1 - - [13/Nov/2022 14:26:44] "GET /static/style.css HTTP/1.1" 404 -
{"items": [{"sugar_g": 12.3, "fiber_g": 2.6, "serving_size_g": 100.0, "sodium_mg": 1, "name": "banana", "potassium_mg": 22, "fat_saturated_g": 0.1, "fat_total_g": 0.3, "calories": 89.4, "cholesterol_mg": 0, "protein_g": 1.1, "carbohydrates_total_g": 23.2}]}
[{'sugar_g': 12.3, 'fiber_g': 2.6, 'serving_size_g': 100.0, 'sodium_mg': 1, 'name': 'banana', 'potassium_mg': 22, 'fat_saturated_g': 0.1, 'fat_total_g': 0.3, 'calories': 89.4, 'cholesterol_mg': 0, 'protein_g': 1.1, 'carbohydrates_total_g': 23.2}]
1/1 [==============================] - 0s 56ms/step
prediction [2]
ORANGE
127.0.0.1 - - [13/Nov/2022 14:27:42] "POST /predict HTTP/1.1" 200 -
127.0.0.1 - - [13/Nov/2022 14:27:42] "GET /static/style.css HTTP/1.1" 404 -
{"items": [{"sugar_g": 8.4, "fiber_g": 2.2, "serving_size_g": 100.0, "sodium_mg": 1, "name": "orange", "potassium_mg": 23, "fat_saturated_g": 0.0, "fat_total_g": 0.1, "calories": 50.4, "cholesterol_mg": 0, "protein_g": 0.9, "carbohydrates_total_g": 12.4}]}
[{'sugar_g': 8.4, 'fiber_g': 2.2, 'serving_size_g': 100.0, 'sodium_mg': 1, 'name': 'orange', 'potassium_mg': 23, 'fat_saturated_g': 0.0, 'fat_total_g': 0.1, 'calories': 50.4, 'cholesterol_mg': 0, 'protein_g': 0.9, 'carbohydrates_total_g': 12.4}]
1/1 [==============================] - 0s 57ms/step
prediction [0]
APPLES
127.0.0.1 - - [13/Nov/2022 14:30:40] "POST /predict HTTP/1.1" 200 -
127.0.0.1 - - [13/Nov/2022 14:30:40] "GET /static/style.css HTTP/1.1" 404 -
{"items": [{"sugar_g": 10.3, "fiber_g": 2.4, "serving_size_g": 100.0, "sodium_mg": 1, "name": "apples", "potassium_mg": 11, "fat_saturated_g": 0.0, "fat_total_g": 0.2, "calories": 53.4, "cholesterol_mg": 0, "protein_g": 0.3, "carbohydrates_total_g": 13.8}]}
[{'sugar_g': 10.3, 'fiber_g': 2.4, 'serving_size_g': 100.0, 'sodium_mg': 1, 'name': 'apples', 'potassium_mg': 11, 'fat_saturated_g': 0.0, 'fat_total_g': 0.2, 'calories': 53.4, 'cholesterol_mg': 0, 'protein_g': 0.3, 'carbohydrates_total_g': 13.8}]
1/1 [==============================] - 0s 48ms/step
prediction [1]
BANANA
127.0.0.1 - - [13/Nov/2022 14:33:03] "POST /predict HTTP/1.1" 200 -
127.0.0.1 - - [13/Nov/2022 14:33:03] "GET /static/style.css HTTP/1.1" 404 -
{"items": [{"sugar_g": 12.3, "fiber_g": 2.6, "serving_size_g": 100.0, "sodium_mg": 1, "name": "banana", "potassium_mg": 22, "fat_saturated_g": 0.1, "fat_total_g": 0.3, "calories": 89.4, "cholesterol_mg": 0, "protein_g": 1.1, "carbohydrates_total_g": 23.2}]}
[{'sugar_g': 12.3, 'fiber_g': 2.6, 'serving_size_g': 100.0, 'sodium_mg': 1, 'name': 'banana', 'potassium_mg': 22, 'fat_saturated_g': 0.1, 'fat_total_g': 0.3, 'calories': 89.4, 'cholesterol_mg': 0, 'protein_g': 1.1, 'carbohydrates_total_g': 23.2}]
1/1 [==============================] - 0s 73ms/step
prediction [4]
WATERMELON
127.0.0.1 - - [13/Nov/2022 14:33:29] "POST /predict HTTP/1.1" 200 -
127.0.0.1 - - [13/Nov/2022 14:33:29] "GET /static/style.css HTTP/1.1" 404 -
{"items": [{"sugar_g": 6.2, "fiber_g": 0.4, "serving_size_g": 100.0, "sodium_mg": 0, "name": "watermelon", "potassium_mg": 10, "fat_saturated_g": 0.0, "fat_total_g": 0.1, "calories": 30.3, "cholesterol_mg": 0, "protein_g": 0.6, "carbohydrates_total_g": 7.4}]}
[{'sugar_g': 6.2, 'fiber_g': 0.4, 'serving_size_g': 100.0, 'sodium_mg': 0, 'name': 'watermelon', 'potassium_mg': 10, 'fat_saturated_g': 0.0, 'fat_total_g': 0.1, 'calories': 30.3, 'cholesterol_mg': 0, 'protein_g': 0.6, 'carbohydrates_total_g': 7.4}]
