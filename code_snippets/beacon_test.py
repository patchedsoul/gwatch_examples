import threading
import pydbus
from gi.repository import GLib


class Beacon:
    """
    <node>
        <interface name='org.bluez.LEAdvertisement1'>
            <method name='Release'>
                <annotation name="org.freedesktop.DBus.Method.NoReply"
value="true"/>
            </method>
            <annotation
name="org.freedesktop.DBus.Properties.PropertiesChanged"
value="const"/>
            <property name="Type" type="s" access="read"/>
            <property name="ServiceUUIDs" type="as" access="read"/>
            <property name="ServiceData" type="a{sv}" access="read"/>
            <property name="IncludeTxPower" type="b" access="read"/>
            <property name="ManufacturerData" type="a{qv}" access="read"/>
            <property name="SolicitUUIDs" type="as" access="read"/>
        </interface>
    </node>
    """
    LE_ADVERTISEMENT_IFACE = 'org.bluez.LEAdvertisement1'

    def Release(self):
        pass

    @property
    def Type(self):
        return 'broadcast'

    @property
    def ServiceUUIDs(self):
        return ['FEAA']

    @property
    def ServiceData(self):
        return {'FEAA': pydbus.Variant('ay', [0x10, 0x08, 0x03, 0x75, 0x6B,
                                              0x42, 0x61, 0x7A, 0x2e, 0x67,
                                              0x69, 0x74, 0x68, 0x75, 0x62,
                                              0x2E, 0x69, 0x6F])}

    @property
    def IncludeTxPower(self):
        return False

    @property
    def ManufacturerData(self):
        return []

    @property
    def SolicitUUIDs(self):
        return []


class LEAdvertisement:
    def __init__(self, service, object_path):
        bus = pydbus.SystemBus()
        bname = bus.request_name(service)
        reg1 = bus.register_object(object_path, Beacon(), None)


class LEAdvertisingManager:
    def __init__(self, object_path):
        lea_iface = 'org.bluez.LEAdvertisingManager1'
        bus = pydbus.SystemBus()
        ad_manager = bus.get('org.bluez', '/org/bluez/hci0')[lea_iface]
        ad_manager.RegisterAdvertisement(object_path, {})
        print('Registered Ad')


def publish_now():
    print('Publishing Ad')
    aloop = GLib.MainLoop()
    aloop.run()


def thread_function():
    print('Starting thread')
    LEAdvertisement(app_name, app_path)
    publish_now()
    print('thread finished')


if __name__ == '__main__':
    app_name = 'ukBaz.bluezero'
    app_path = '/ukBaz/bluezero/advertisement0099'

    loop = GLib.MainLoop()
    x = threading.Thread(target=thread_function, daemon=True)
    x.start()
    LEAdvertisingManager(app_path)

    try:
        loop.run()
    except KeyboardInterrupt:
        print("\nStopping ...")
        loop.quit()