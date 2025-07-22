FROM nginx:stable-alpine

COPY app/index.html /usr/share/nginx/html/index.html
COPY app/nginx.conf /etc/nginx/nginx.conf

EXPOSE 80

HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 \
  CMD curl --fail http://localhost/ || exit 1