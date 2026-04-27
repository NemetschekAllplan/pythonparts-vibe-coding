<?xml version="1.0" encoding="utf-8"?>
<Element xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:noNamespaceSchemaLocation="https://pythonparts.allplan.com/2026/schemas/PythonPart.xsd">
    <Script>
        <Name>Pergola_ZProfil.py</Name>
        <Title>Pergola Z-Profil</Title>
        <Version>1.0</Version>
        <Interactor>False</Interactor>
        <ReadLastInput>True</ReadLastInput>
    </Script>

    <Page>
        <Name>MainPage</Name>
        <Text>Pergola</Text>
        <Parameters>
            <Parameter>
                <Name>TragstrukturExpander</Name>
                <Text>Tragstruktur</Text>
                <Value>True</Value>
                <ValueType>Expander</ValueType>
                <Parameters>
                    <Parameter>
                        <Name>Breite</Name>
                        <Text>Breite [mm]</Text>
                        <Value>4000</Value>
                        <ValueType>Length</ValueType>
                        <MinValue>1000</MinValue>
                        <MaxValue>12000</MaxValue>
                    </Parameter>
                    <Parameter>
                        <Name>Tiefe</Name>
                        <Text>Tiefe [mm]</Text>
                        <Value>3000</Value>
                        <ValueType>Length</ValueType>
                        <MinValue>1000</MinValue>
                        <MaxValue>8000</MaxValue>
                    </Parameter>
                    <Parameter>
                        <Name>Hoehe</Name>
                        <Text>Hoehe [mm]</Text>
                        <Value>2500</Value>
                        <ValueType>Length</ValueType>
                        <MinValue>2000</MinValue>
                        <MaxValue>4000</MaxValue>
                    </Parameter>
                    <Parameter>
                        <Name>PfostenBreite</Name>
                        <Text>Pfostenbreite [mm]</Text>
                        <Value>120</Value>
                        <ValueType>Length</ValueType>
                        <MinValue>80</MinValue>
                        <MaxValue>200</MaxValue>
                    </Parameter>
                    <Parameter>
                        <Name>RahmenHoehe</Name>
                        <Text>Rahmenhoehe [mm]</Text>
                        <Value>100</Value>
                        <ValueType>Length</ValueType>
                        <MinValue>50</MinValue>
                        <MaxValue>200</MaxValue>
                    </Parameter>
                    <Parameter>
                        <Name>RahmenBreite</Name>
                        <Text>Rahmenbreite [mm]</Text>
                        <Value>80</Value>
                        <ValueType>Length</ValueType>
                        <MinValue>50</MinValue>
                        <MaxValue>200</MaxValue>
                    </Parameter>
                </Parameters>
            </Parameter>

            <Parameter>
                <Name>LamellenExpander</Name>
                <Text>Lamellen</Text>
                <Value>True</Value>
                <ValueType>Expander</ValueType>
                <Parameters>
                    <Parameter>
                        <Name>LamellenBreite</Name>
                        <Text>Lamellenbreite [mm]</Text>
                        <Value>200</Value>
                        <ValueType>Length</ValueType>
                        <MinValue>100</MinValue>
                        <MaxValue>300</MaxValue>
                    </Parameter>
                    <Parameter>
                        <Name>LamellenHoehe</Name>
                        <Text>Lamellenhoehe [mm]</Text>
                        <Value>20</Value>
                        <ValueType>Length</ValueType>
                        <MinValue>15</MinValue>
                        <MaxValue>80</MaxValue>
                    </Parameter>
                    <Parameter>
                        <Name>LamellenStaerke</Name>
                        <Text>Lamellenstaerke [mm]</Text>
                        <Value>2</Value>
                        <ValueType>Length</ValueType>
                        <MinValue>1</MinValue>
                        <MaxValue>5</MaxValue>
                    </Parameter>
                    <Parameter>
                        <Name>LamellenAnzahl</Name>
                        <Text>Lamellenanzahl</Text>
                        <Value>15</Value>
                        <ValueType>Integer</ValueType>
                        <MinValue>3</MinValue>
                        <MaxValue>50</MaxValue>
                    </Parameter>
                    <Parameter>
                        <Name>LamellenStellung</Name>
                        <Text>Lamellenstellung</Text>
                        <Value>Geschlossen</Value>
                        <ValueList>Geschlossen|Halboffen|Offen</ValueList>
                        <ValueType>StringComboBox</ValueType>
                    </Parameter>
                </Parameters>
            </Parameter>
        </Parameters>
    </Page>
</Element>
