package com.vungle.publisher;
import android.app.Service;
import android.content.Intent;
import android.os.IBinder;

public class VungleService extends Service {

    public VungleService() {
    }

    @Override
    public IBinder onBind(Intent intent) {
      return null;
    }
}
