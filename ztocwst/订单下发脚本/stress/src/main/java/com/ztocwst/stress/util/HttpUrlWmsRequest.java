package com.ztocwst.stress.util;

import org.apache.http.HttpEntity;
import org.apache.http.HttpResponse;
import org.apache.http.HttpStatus;
import org.apache.http.client.methods.CloseableHttpResponse;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.entity.StringEntity;
import org.apache.http.impl.client.CloseableHttpClient;
import org.apache.http.impl.client.HttpClients;
import org.apache.http.util.EntityUtils;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.io.IOException;
import java.nio.charset.Charset;
import java.util.Map;

/**
 * @className: HttpUrlRequest
 * @description: TODO
 * @author: LiuQu
 * @date:
 * @version: 1.0
 */
public class HttpUrlWmsRequest {

    private static Logger logger = LoggerFactory.getLogger(HttpUrlWmsRequest.class);

    /**
     * 向指定 URL 发送POST方法的请求
     * @param url 发送请求的 URL
     * @param body 请求的数据体
     * @return 远程资源的响应结果
     */
    public static String sendPostQiMen(String url, String body) throws IOException {
        CloseableHttpClient httpClient = HttpClients.createDefault();
        HttpPost httpPost = new HttpPost(url);
        httpPost.addHeader("Content-Type", "application/xml;charset=utf-8");
        httpPost.setEntity(new StringEntity(body.toString(), Charset.forName("UTF-8")));
        httpPost.setHeader("Accept", "application/xml");
        CloseableHttpResponse response = httpClient.execute(httpPost);
//        System.out.println(response.getStatusLine().getStatusCode() + "\n");
        HttpEntity entity = response.getEntity();
        String responseContent = EntityUtils.toString(entity, "UTF-8");
//        System.out.println(responseContent);
        response.close();
        httpClient.close();
        return responseContent;
    }
    public static String sendPost01(String url, String body) throws IOException {
        CloseableHttpClient httpClient = HttpClients.createDefault();
        HttpPost httpPost = new HttpPost(url);
        httpPost.addHeader("Content-Type", "application/json;charset=utf-8");
        if(body != null){
            httpPost.setEntity(new StringEntity(body.toString(), Charset.forName("UTF-8")));
        }
        httpPost.setHeader("Accept", "application/json");
        CloseableHttpResponse response = httpClient.execute(httpPost);
        System.out.println(response.getStatusLine().getStatusCode() + "\n");
        HttpEntity entity = response.getEntity();
        String responseContent = EntityUtils.toString(entity, "UTF-8");
        System.out.println(responseContent);
        response.close();
        httpClient.close();
        return responseContent;
    }

    public static String httpPostWithParams(Map<String,Object> params, String url){
        HttpResponse response = null;
        CloseableHttpClient closeableHttpClient = null;
        String responseStr = null ;
        try {
            closeableHttpClient = HttpClients.createDefault();
            HttpPost post = new HttpPost(url);

            // 构造消息头
            post.setHeader("Content-type", "application/x-www-form-urlencoded");

            String body = "";
            for(Map.Entry<String,Object> entry : params.entrySet()){
                body = body+ entry.getKey()+"="+entry.getValue()+"&" ;
            }
            body = body.substring(0,body.length()-1);
            logger.info("httpPostWithParams ,body:{}",body);
            // 构建消息实体
            StringEntity entity = new StringEntity(body, Charset.forName("UTF-8"));

            // 发送Json格式的数据请求
            entity.setContentType("application/json");
            post.setEntity(entity);

            response = closeableHttpClient.execute(post);
            if(HttpStatus.SC_OK != response.getStatusLine().getStatusCode()){
                return null;
            }
            HttpEntity httpEntity = response.getEntity();
            logger.info("httpEntity:{}",httpEntity);
            try {
                responseStr = EntityUtils.toString(httpEntity, Charset.forName("UTF-8"));
            } catch (IOException e) {
                logger.error("EntityUtils.toString error",e);
            }
            return responseStr;
        } catch (Exception e) {
            logger.error("httpPostWithJson Exception",e);
        }finally{
            try {
                if(response != null){
                    ((CloseableHttpResponse) response).close();
                }
                if(closeableHttpClient != null){
                    closeableHttpClient.close();
                }
            } catch (IOException e) {
                logger.error("httpPostWithJson IOException ",e);
            }
        }
        return responseStr;
    }
}
