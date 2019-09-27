package com.ztocwst.stress.domain;

import java.time.LocalDateTime;
import java.time.ZoneOffset;

/**
 * @version v1.0
 * @program: stress
 * @description:
 * @author: mulan
 * @create: 2019-06-25 13:53
 **/
public class BJSL001MessageDTO {

    private String body;

    private String url="http://47.111.166.135:30017/api/edi/qimen/in?method=deliveryorder.create&timestamp=2018-11-21%3000:00:00&format=xml&app_key&v=1.0&sign&sign_method=md5&customerId=BJSL001";

    private String[] code;

    private Long no;

    public BJSL001MessageDTO(String[] code) {
        this.code = code;
    }

    public String getBody() {
        int num1 = (int)((Math.random()*9+1)*100000);
        int num2 = (int)((Math.random()*9+1)*100000);


        BJSL001ItemDTO itemDTO = new BJSL001ItemDTO(code);
        body = "<?xml version=\"1.0\" encoding=\"utf-8\"?>\n" +
                "<request>\n" +
                "  <deliveryOrder>\n" +
                "    <arAmount>0.0</arAmount>\n" +
                "    <buyerMessage/>\n" +
                "    <buyerNick>崔俊锋</buyerNick>\n" +
                "    <createTime>2019-06-25 13:57:17</createTime>\n" +
                "    <deliveryOrderCode>CWST"+no+"</deliveryOrderCode>\n" +
                "    <extendProps>\n" +
                "      <key1>null</key1>\n" +
                "      <routeCode>null</routeCode>\n" +
                "      <key2>null</key2>\n" +
                "      <isThreePL>N</isThreePL>\n" +
                "      <key3>null</key3>\n" +
                "      <isJitx>false</isJitx>\n" +
                "      <vendorId>null</vendorId>\n" +
                "      <shopId>null</shopId>\n" +
                "      <storeCode>tb_bmhtqjd</storeCode>\n" +
                "    </extendProps>\n" +
                "    <freight>0.0</freight>\n" +
                "    <gotAmount>135.0</gotAmount>\n" +
                "    <invoiceFlag>N</invoiceFlag>\n" +
                "    <isUrgency>N</isUrgency>\n" +
                "    <itemAmount>135.0</itemAmount>\n" +
                "    <logisticsCode>ZTO</logisticsCode>\n" +
                "    <logisticsName>中通快递</logisticsName>\n" +
                "    <expressCode>"+num1+""+num2+"</expressCode> "+
                "    <operateTime>2019-06-25 13:57:17</operateTime>\n" +
                "    <orderFlag/>\n" +
                "    <orderType>JYCK</orderType>\n" +
                "    <ownerCode>BJSL001</ownerCode>\n" +
                "    <payTime>2019-06-25 13:42:15</payTime>\n" +
                "    <placeOrderTime>2019-06-25 13:57:17</placeOrderTime>\n" +
                "    <receiverInfo>\n" +
                "      <area>余杭区</area>\n" +
                "      <city>杭州市</city>\n" +
                "      <countryCode>1</countryCode>\n" +
                "      <detailAddress>浙江省 杭州市 余杭区 未来科技城研创园520室</detailAddress>\n" +
                "      <mobile>18158685663</mobile>\n" +
                "      <name>崔俊锋</name>\n" +
                "      <province>浙江省</province>\n" +
                "      <zipCode>310012</zipCode>\n" +
                "    </receiverInfo>\n" +
                "    <remark/>\n" +
                "    <sellerMessage/>\n" +
                "    <sellerNick>天猫_半亩花田旗舰店</sellerNick>\n" +
                "    <senderInfo>\n" +
                "      <area>花都区</area>\n" +
                "      <city>广州市</city>\n" +
                "      <countryCode>CN</countryCode>\n" +
                "      <detailAddress>广州市花山镇起源大道14号中通花山分拨中心</detailAddress>\n" +
                "      <name>1</name>\n" +
                "      <province>广东省</province>\n" +
                "    </senderInfo>\n" +
                "    <shopNick>天猫_半亩花田旗舰店</shopNick>\n" +
                "    <sourcePlatformCode>TM</sourcePlatformCode>\n" +
                "    <sourcePlatformName>TMALL</sourcePlatformName>\n" +
                "    <totalAmount>135.0</totalAmount>\n" +
                "    <warehouseCode>023-007K</warehouseCode>\n" +
                "  </deliveryOrder>\n" +
                "  <orderLines>\n" +
                itemDTO.getItemString()+
                "  </orderLines>\n" +
                "</request>";
//        body.replace("<deliveryOrderCode>CWST</deliveryOrderCode>","<deliveryOrderCode>CWST20190625"+no+"</deliveryOrderCode>");
        return body;
    }

    public void setBody(String body) {
        this.body = body;
    }

    public Long getNo() {
        Long s = LocalDateTime.now().toEpochSecond(ZoneOffset.of("+8")) + (int)(1+Math.random()*(100000000-1+1));
        return s;
    }

    public String getUrl() {
        return url;
    }

    public void setUrl(String url) {
        this.url = url;
    }

    public void setNo(Long no) {
        this.no = no;
    }
}
