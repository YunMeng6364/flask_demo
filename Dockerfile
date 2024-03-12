# 使用官方 Python 运行时作为父镜像
FROM python:3.8-slim

# 设置工作目录为 /app
WORKDIR /app

# 将当前目录内容复制到位于 /app 中的容器中
COPY . /app

# 安装 requirements.txt 中指定的任何所需包
# 假设你的项目根目录下有一个 requirements.txt 文件
#RUN pip install --no-cache-dir -r requirements.txt -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com
# 下载安装flask
RUN pip3 install flask

# 让端口 5000 可用于外界访问
EXPOSE 5000

# 在容器启动时运行 app.py
# 假设你的 Flask 应用的入口点是 app.py
CMD ["python", "app.py"]