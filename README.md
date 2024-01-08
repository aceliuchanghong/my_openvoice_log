# my_openvoice_log

my_openvoice_log

### purpose

build a saas in server then give api,so i can use

* 语音转文字==>faster-whisper git@github.com:SYSTRAN/faster-whisper.git
* 文字转语音 声音克隆==>OpenVoice git@github.com:myshell-ai/OpenVoice.git
* llm==>ChatGLM git@github.com:THUDM/ChatGLM3.git LLaMA-7B
* sd的lora也可以试试==>之后再说

### install
#pip list --format=freeze > requirements.txt
#distribute，pip，setuptools，wheel 需要删除

git clone git@github.com:aceliuchanghong/my_openvoice_log.git

conda create -n OpenVoice python=3.10

conda activate OpenVoice

pip install -r requirements.txt --proxy=127.0.0.1:10809
conda install pytorch==1.13.1 torchvision==0.14.1 torchaudio==0.13.1 pytorch-cuda=11.7 -c pytorch -c nvidia
```
# 修改conda的配置文件 .condarc 文件，路径为C:\Users\XXXX
channels:
  - defaults
show_channel_urls: true
proxy_servers:
  http: http://127.0.0.1:10809
  https: http://127.0.0.1:10809
ssl_verify: true
```
## 查看cuda版本和占用情况
nvidia-smi
