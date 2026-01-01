# 🚀 Deployment Guide

Guide for deploying the GxP Validation Assistant to production environments.

## Deployment Options

### Option 1: Streamlit Cloud (Recommended for Demo)

#### Prerequisites
- GitHub account
- Streamlit Cloud account (free at [streamlit.io/cloud](https://streamlit.io/cloud))

#### Steps

1. **Push to GitHub**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin <your-repo-url>
   git push -u origin main
   ```

2. **Deploy on Streamlit Cloud**
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Click "New app"
   - Select your repository
   - Set main file path: `app.py`
   - Add secrets in "Advanced settings":
     ```
     GOOGLE_API_KEY = "your_api_key_here"
     ```

3. **Initialize Database**
   - After first deployment, access the app
   - The database will need to be initialized
   - Note: Large PDF processing may timeout on free tier

#### Limitations
- Free tier has resource limits
- May need to reduce document size or chunk count
- Database resets on app restart

---

### Option 2: Docker Deployment

#### Create Dockerfile

```dockerfile
FROM python:3.9-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY . .

# Create necessary directories
RUN mkdir -p logs vector_db

# Expose Streamlit port
EXPOSE 8501

# Initialize database and run app
CMD python initialize_db.py && streamlit run app.py --server.port=8501 --server.address=0.0.0.0
```

#### Build and Run

```bash
# Build image
docker build -t gxp-assistant .

# Run container
docker run -p 8501:8501 \
  -e GOOGLE_API_KEY=your_api_key_here \
  -v $(pwd)/vector_db:/app/vector_db \
  gxp-assistant
```

---

### Option 3: Cloud VM (AWS/GCP/Azure)

#### Setup on Ubuntu Server

1. **Install Python and dependencies**
   ```bash
   sudo apt update
   sudo apt install python3.9 python3-pip
   ```

2. **Clone repository**
   ```bash
   git clone <your-repo-url>
   cd GxP-Validation-Assistant
   ```

3. **Install requirements**
   ```bash
   pip3 install -r requirements.txt
   ```

4. **Configure environment**
   ```bash
   cp .env.example .env
   nano .env  # Add your API key
   ```

5. **Initialize database**
   ```bash
   python3 initialize_db.py
   ```

6. **Run with systemd (persistent service)**

   Create `/etc/systemd/system/gxp-assistant.service`:
   ```ini
   [Unit]
   Description=GxP Validation Assistant
   After=network.target

   [Service]
   Type=simple
   User=ubuntu
   WorkingDirectory=/home/ubuntu/GxP-Validation-Assistant
   Environment="PATH=/home/ubuntu/.local/bin"
   ExecStart=/usr/bin/python3 -m streamlit run app.py --server.port=8501 --server.address=0.0.0.0
   Restart=always

   [Install]
   WantedBy=multi-user.target
   ```

   Enable and start:
   ```bash
   sudo systemctl enable gxp-assistant
   sudo systemctl start gxp-assistant
   ```

7. **Setup Nginx reverse proxy**
   ```nginx
   server {
       listen 80;
       server_name your-domain.com;

       location / {
           proxy_pass http://localhost:8501;
           proxy_http_version 1.1;
           proxy_set_header Upgrade $http_upgrade;
           proxy_set_header Connection "upgrade";
           proxy_set_header Host $host;
       }
   }
   ```

---

### Option 4: Heroku

#### Prerequisites
- Heroku account and CLI installed

#### Files needed

**Procfile**
```
web: sh setup.sh && streamlit run app.py
```

**setup.sh**
```bash
mkdir -p ~/.streamlit/

echo "\
[server]\n\
headless = true\n\
port = $PORT\n\
enableCORS = false\n\
\n\
" > ~/.streamlit/config.toml
```

#### Deploy
```bash
heroku create gxp-validation-assistant
heroku config:set GOOGLE_API_KEY=your_api_key_here
git push heroku main
```

---

## Production Considerations

### Security

1. **API Key Management**
   - Never commit `.env` file
   - Use environment variables or secret managers
   - Rotate keys regularly

2. **Access Control**
   - Add authentication (Streamlit supports basic auth)
   - Use HTTPS in production
   - Implement rate limiting

3. **Data Privacy**
   - Ensure compliance with data protection regulations
   - Log access and queries for audit trails
   - Consider data residency requirements

### Performance Optimization

1. **Caching**
   - Vector store is cached with `@st.cache_resource`
   - Consider Redis for distributed caching

2. **Database**
   - Use persistent volume for vector database
   - Regular backups of vector_db folder
   - Consider managed vector DB (Pinecone, Weaviate)

3. **Scaling**
   - Use load balancer for multiple instances
   - Separate embedding generation from query serving
   - Consider async processing for large documents

### Monitoring

1. **Logging**
   - All logs stored in `logs/` folder
   - Use centralized logging (ELK, CloudWatch)
   - Monitor error rates and response times

2. **Metrics**
   - Track query volume and patterns
   - Monitor API usage and costs
   - Set up alerts for failures

3. **Health Checks**
   - Implement `/health` endpoint
   - Monitor database connectivity
   - Check API key validity

### Cost Optimization

1. **Gemini API**
   - Monitor token usage
   - Implement query caching
   - Set rate limits per user

2. **Infrastructure**
   - Use auto-scaling based on load
   - Shut down dev instances when not in use
   - Consider reserved instances for production

### Backup and Recovery

1. **Vector Database**
   ```bash
   # Backup
   tar -czf vector_db_backup_$(date +%Y%m%d).tar.gz vector_db/
   
   # Restore
   tar -xzf vector_db_backup_YYYYMMDD.tar.gz
   ```

2. **Configuration**
   - Version control all config files
   - Document environment variables
   - Keep secrets in secure vault

### Maintenance

1. **Updates**
   - Regular dependency updates
   - Test in staging before production
   - Monitor for security vulnerabilities

2. **Database Refresh**
   - Schedule periodic reindexing
   - Add new documents as needed
   - Remove outdated content

---

## Environment Variables

| Variable | Description | Required | Default |
|----------|-------------|----------|---------|
| GOOGLE_API_KEY | Google Gemini API key | Yes | - |
| APP_TITLE | Application title | No | GxP Validation Assistant |
| APP_ICON | Application icon | No | 🏥 |
| MAX_TOKENS | Max response tokens | No | 2048 |
| TEMPERATURE | Model temperature | No | 0.3 |
| TOP_K | Documents to retrieve | No | 5 |

---

## Testing in Production

1. **Smoke Tests**
   ```bash
   python test_system.py
   ```

2. **Load Testing**
   - Use tools like Locust or JMeter
   - Test concurrent users
   - Monitor response times

3. **Integration Tests**
   - Test all API endpoints
   - Verify database connectivity
   - Check error handling

---

## Support and Maintenance

### Regular Tasks
- [ ] Weekly: Check logs for errors
- [ ] Monthly: Update dependencies
- [ ] Quarterly: Review and update documents
- [ ] Yearly: Audit security and compliance

### Incident Response
1. Check application logs
2. Verify API key validity
3. Check database connectivity
4. Review recent changes
5. Rollback if necessary

---

## Compliance Notes

For GxP environments, ensure:
- ✅ Audit trails enabled
- ✅ Access controls implemented
- ✅ Data integrity maintained
- ✅ Change control process
- ✅ Validation documentation
- ✅ Disaster recovery plan

---

**Questions?** Refer to the main [README.md](README.md) for more details.
