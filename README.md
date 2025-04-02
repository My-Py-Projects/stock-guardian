# StockGuardian - Financial Alert System

## 🎯 Project Description  
Automated stock monitoring system that sends WhatsApp alerts with price variations and relevant news articles for specified companies.

## 📦 Deliverables  
- Dual API integration (financial data + news)  
- Dynamic message formatting system  
- Error-resistant stock data retrieval  
- Secure credential management  

## 🚀 Key Features  
- 📈 Real-time stock price tracking  
- 📰 Integrated news feed aggregation  
- ⚡ Automated alert triggers  
- 📊 Percentage change calculations  
- 🔄 Fallback mechanism for market closures  

## 🛠️ Technologies Used  
| Component              | Technology                          |
|------------------------|-------------------------------------|
| **Language**           | Python 3                            |
| **Stock API**          | Alpha Vantage                       |
| **News API**           | NewsAPI                             |
| **Messaging**          | Twilio                              |
| **Env Management**     | python-dotenv                       |
| **Date Handling**      | datetime                            |

## ⚙️ Installation & Setup  

### 1. Clone Repository  
```bash
git clone https://github.com/My-Py-Projects/stock-guardian.git
cd stock-guardian
```

### 2. Install Dependencies  
```bash
pip install requests python-dotenv twilio
```

### 3. Environment Configuration  
Create `.env` file in root directory with:

```ini
# Alpha Vantage
API_KEY_STOCK=your_alpha_vantage_key

# NewsAPI
API_KEY_NEWS=your_newsapi_key

# Twilio
TWILIO_SID=your_account_sid
TWILIO_AUTH_TOKEN=your_auth_token
TWILIO_PHONE=whatsapp:+1415523...
USER_PHONE=whatsapp:+5511...
```

### 4. Run Application  
```bash
python main.py
```

**Important Notes:**  
```plaintext
1. Required API Accounts:
   - Alpha Vantage: https://www.alphavantage.co
   - NewsAPI: https://newsapi.org
   - Twilio: https://www.twilio.com

2. Stock Data Considerations:
   - Uses latest available trading days
   - Handles market closure dates automatically
```