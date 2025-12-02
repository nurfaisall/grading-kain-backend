# Flask Backend - Simple

Kerangka kerja Flask yang sederhana dan minimalis.

## 📁 Struktur

```
fabric-grading-dashboard-backend/
├── app.py              # Aplikasi Flask utama
├── requirements.txt    # Dependencies
└── README.md          # Dokumentasi
```

## 🚀 Cara Memulai

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Jalankan aplikasi
python app.py
```

Aplikasi akan berjalan di `http://localhost:5000`

## 🔌 API Endpoints

- `GET /` - Welcome message
- `GET /health` - Health check
- `GET /api/data` - Get data
- `POST /api/data` - Create data

## 📝 Contoh Request

### GET Data
```bash
curl http://localhost:5000/api/data
```

### POST Data
```bash
curl -X POST http://localhost:5000/api/data \
  -H "Content-Type: application/json" \
  -d '{"name": "New Item"}'
```

## 🛠️ Pengembangan

Tambahkan route baru di `app.py`:

```python
@app.route('/api/your-endpoint', methods=['GET'])
def your_function():
    return jsonify({'message': 'Hello'})
```
