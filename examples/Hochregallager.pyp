<?xml version="1.0" encoding="utf-8"?>
<Element xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:noNamespaceSchemaLocation="https://pythonparts.allplan.com/2026/schemas/PythonPart.xsd">
    <Script>
        <Name>Hochregallager.py</Name>
        <Title>Hochregallager</Title>
        <Version>3.0</Version>
        <ReadLastInput>True</ReadLastInput>
    </Script>

    <Page>
        <Name>PageRaster</Name>
        <Text>Raster</Text>
        <Parameters>
            <Parameter>
                <Name>FieldCountX</Name>
                <Text>Anzahl Felder X</Text>
                <Value>3</Value>
                <ValueType>Integer</ValueType>
                <MinValue>1</MinValue>
                <MaxValue>100</MaxValue>
            </Parameter>
            <Parameter>
                <Name>FieldCountY</Name>
                <Text>Anzahl Reihen Y</Text>
                <Value>1</Value>
                <ValueType>Integer</ValueType>
                <MinValue>1</MinValue>
                <MaxValue>50</MaxValue>
                <Visible>DoubleRack == False</Visible>
                <Enable>DoubleRack == False</Enable>
            </Parameter>
            <Parameter>
                <Name>LevelCountZ</Name>
                <Text>Anzahl Ebenen Z</Text>
                <Value>3</Value>
                <ValueType>Integer</ValueType>
                <MinValue>1</MinValue>
                <MaxValue>20</MaxValue>
            </Parameter>
            <Parameter>
                <Name>FieldWidth</Name>
                <Text>Feldbreite</Text>
                <Value>2700</Value>
                <ValueType>Length</ValueType>
                <MinValue>500</MinValue>
                <MaxValue>20000</MaxValue>
            </Parameter>
            <Parameter>
                <Name>FieldDepth</Name>
                <Text>Regaltiefe</Text>
                <Value>1100</Value>
                <ValueType>Length</ValueType>
                <MinValue>300</MinValue>
                <MaxValue>5000</MaxValue>
            </Parameter>
            <Parameter>
                <Name>LevelHeight</Name>
                <Text>Ebenenhoehe</Text>
                <Value>1800</Value>
                <ValueType>Length</ValueType>
                <MinValue>500</MinValue>
                <MaxValue>5000</MaxValue>
            </Parameter>
            <Parameter>
                <Name>RasterSep1</Name>
                <Text></Text>
                <ValueType>Separator</ValueType>
            </Parameter>
            <Parameter>
                <Name>DoubleRack</Name>
                <Text>Doppelregal</Text>
                <Value>False</Value>
                <ValueType>CheckBox</ValueType>
            </Parameter>
            <Parameter>
                <Name>AisleWidth</Name>
                <Text>Gangbreite</Text>
                <Value>3000</Value>
                <ValueType>Length</ValueType>
                <MinValue>1000</MinValue>
                <MaxValue>10000</MaxValue>
                <Visible>DoubleRack == True</Visible>
                <Enable>DoubleRack == True</Enable>
            </Parameter>
            <Parameter>
                <Name>RowSpacing</Name>
                <Text>Reihenabstand</Text>
                <Value>3000</Value>
                <ValueType>Length</ValueType>
                <MinValue>1000</MinValue>
                <MaxValue>10000</MaxValue>
                <Visible>DoubleRack == False and FieldCountY > 1</Visible>
                <Enable>DoubleRack == False and FieldCountY > 1</Enable>
            </Parameter>
        </Parameters>
    </Page>

    <Page>
        <Name>PageProfile</Name>
        <Text>Profile</Text>
        <Parameters>
            <Parameter>
                <Name>PostWidth</Name>
                <Text>Stuetzenbreite</Text>
                <Value>80</Value>
                <ValueType>Length</ValueType>
                <MinValue>30</MinValue>
                <MaxValue>500</MaxValue>
            </Parameter>
            <Parameter>
                <Name>PostDepth</Name>
                <Text>Stuetzentiefe</Text>
                <Value>83</Value>
                <ValueType>Length</ValueType>
                <MinValue>30</MinValue>
                <MaxValue>500</MaxValue>
            </Parameter>
            <Parameter>
                <Name>BeamHeight</Name>
                <Text>Traversenhoehe</Text>
                <Value>120</Value>
                <ValueType>Length</ValueType>
                <MinValue>30</MinValue>
                <MaxValue>500</MaxValue>
            </Parameter>
            <Parameter>
                <Name>BeamDepth</Name>
                <Text>Traversentiefe</Text>
                <Value>50</Value>
                <ValueType>Length</ValueType>
                <MinValue>10</MinValue>
                <MaxValue>300</MaxValue>
            </Parameter>
            <Parameter>
                <Name>BeamCapacity</Name>
                <Text>Traversentragfaehigkeit (kg)</Text>
                <Value>3000</Value>
                <ValueType>Double</ValueType>
                <MinValue>0</MinValue>
                <MaxValue>99999</MaxValue>
            </Parameter>
        </Parameters>
    </Page>

    <Page>
        <Name>PageOptions</Name>
        <Text>Optionen</Text>
        <Parameters>
            <Parameter>
                <Name>ShowGroundBeams</Name>
                <Text>Traversen auf Grundebene</Text>
                <Value>False</Value>
                <ValueType>CheckBox</ValueType>
            </Parameter>
            <Parameter>
                <Name>OptionSep0</Name>
                <Text></Text>
                <ValueType>Separator</ValueType>
            </Parameter>

            <Parameter>
                <Name>ShelfExpanderOpen</Name>
                <Text>Regalboeden</Text>
                <Value>True</Value>
                <ValueType>Expander</ValueType>
                <Parameters>
                    <Parameter>
                        <Name>ShowShelves</Name>
                        <Text>Regalboeden anzeigen</Text>
                        <Value>True</Value>
                        <ValueType>CheckBox</ValueType>
                    </Parameter>
                    <Parameter>
                        <Name>ShelfThickness</Name>
                        <Text>Bodendicke</Text>
                        <Value>20</Value>
                        <ValueType>Length</ValueType>
                        <MinValue>5</MinValue>
                        <MaxValue>200</MaxValue>
                        <Visible>ShowShelves == True</Visible>
                    </Parameter>
                    <Parameter>
                        <Name>ShowGroundShelf</Name>
                        <Text>Boden auf Grundebene</Text>
                        <Value>False</Value>
                        <ValueType>CheckBox</ValueType>
                        <Visible>ShowShelves == True</Visible>
                    </Parameter>
                </Parameters>
            </Parameter>

            <Parameter>
                <Name>BracingExpanderOpen</Name>
                <Text>Verbaende</Text>
                <Value>True</Value>
                <ValueType>Expander</ValueType>
                <Parameters>
                    <Parameter>
                        <Name>ShowBracing</Name>
                        <Text>Diagonalverbaende anzeigen</Text>
                        <Value>True</Value>
                        <ValueType>CheckBox</ValueType>
                    </Parameter>
                    <Parameter>
                        <Name>BracingDepth</Name>
                        <Text>Verbandstiefe</Text>
                        <Value>30</Value>
                        <ValueType>Length</ValueType>
                        <MinValue>10</MinValue>
                        <MaxValue>200</MaxValue>
                        <Visible>ShowBracing == True</Visible>
                    </Parameter>
                    <Parameter>
                        <Name>BracingWidth</Name>
                        <Text>Verbandsbreite</Text>
                        <Value>30</Value>
                        <ValueType>Length</ValueType>
                        <MinValue>10</MinValue>
                        <MaxValue>200</MaxValue>
                        <Visible>ShowBracing == True</Visible>
                    </Parameter>
                </Parameters>
            </Parameter>

            <Parameter>
                <Name>BasePlateExpanderOpen</Name>
                <Text>Fussplatten</Text>
                <Value>True</Value>
                <ValueType>Expander</ValueType>
                <Parameters>
                    <Parameter>
                        <Name>ShowBasePlates</Name>
                        <Text>Fussplatten anzeigen</Text>
                        <Value>True</Value>
                        <ValueType>CheckBox</ValueType>
                    </Parameter>
                    <Parameter>
                        <Name>BasePlateLength</Name>
                        <Text>Fussplatte Laenge (X)</Text>
                        <Value>150</Value>
                        <ValueType>Length</ValueType>
                        <MinValue>50</MinValue>
                        <MaxValue>500</MaxValue>
                        <Visible>ShowBasePlates == True</Visible>
                    </Parameter>
                    <Parameter>
                        <Name>BasePlateWidth</Name>
                        <Text>Fussplatte Breite (Y)</Text>
                        <Value>118</Value>
                        <ValueType>Length</ValueType>
                        <MinValue>50</MinValue>
                        <MaxValue>500</MaxValue>
                        <Visible>ShowBasePlates == True</Visible>
                    </Parameter>
                    <Parameter>
                        <Name>BasePlateThickness</Name>
                        <Text>Fussplatte Dicke</Text>
                        <Value>5</Value>
                        <ValueType>Length</ValueType>
                        <MinValue>2</MinValue>
                        <MaxValue>100</MaxValue>
                        <Visible>ShowBasePlates == True</Visible>
                    </Parameter>
                </Parameters>
            </Parameter>

        </Parameters>
    </Page>

    <Page>
        <Name>PagePallets</Name>
        <Text>Paletten</Text>
        <Parameters>
            <Parameter>
                <Name>PalletExpander</Name>
                <Text>Paletten-Anzeige</Text>
                <Value>True</Value>
                <ValueType>Expander</ValueType>
                <Parameters>
                    <Parameter>
                        <Name>ShowPallets</Name>
                        <Text>Paletten anzeigen</Text>
                        <Value>True</Value>
                        <ValueType>CheckBox</ValueType>
                    </Parameter>
                    <Parameter>
                        <Name>PalletLength</Name>
                        <Text>Palettenlaenge</Text>
                        <Value>1200</Value>
                        <ValueType>Length</ValueType>
                        <MinValue>200</MinValue>
                        <MaxValue>3000</MaxValue>
                        <Visible>ShowPallets == True</Visible>
                    </Parameter>
                    <Parameter>
                        <Name>PalletWidth</Name>
                        <Text>Palettenbreite</Text>
                        <Value>800</Value>
                        <ValueType>Length</ValueType>
                        <MinValue>200</MinValue>
                        <MaxValue>2000</MaxValue>
                        <Visible>ShowPallets == True</Visible>
                    </Parameter>
                    <Parameter>
                        <Name>PalletHeight</Name>
                        <Text>Palettenhoehe</Text>
                        <Value>144</Value>
                        <ValueType>Length</ValueType>
                        <MinValue>50</MinValue>
                        <MaxValue>500</MaxValue>
                        <Visible>ShowPallets == True</Visible>
                    </Parameter>
                    <Parameter>
                        <Name>PalletsPerField</Name>
                        <Text>Paletten pro Feld</Text>
                        <Value>2</Value>
                        <ValueType>Integer</ValueType>
                        <MinValue>1</MinValue>
                        <MaxValue>4</MaxValue>
                        <Visible>ShowPallets == True</Visible>
                    </Parameter>
                    <Parameter>
                        <Name>PalletGapX</Name>
                        <Text>Palettenabstand X</Text>
                        <Value>100</Value>
                        <ValueType>Length</ValueType>
                        <MinValue>0</MinValue>
                        <MaxValue>500</MaxValue>
                        <Visible>ShowPallets == True</Visible>
                    </Parameter>
                    <Parameter>
                        <Name>PalletGapY</Name>
                        <Text>Palettenabstand Y</Text>
                        <Value>50</Value>
                        <ValueType>Length</ValueType>
                        <MinValue>0</MinValue>
                        <MaxValue>500</MaxValue>
                        <Visible>ShowPallets == True</Visible>
                    </Parameter>
                </Parameters>
            </Parameter>

            <Parameter>
                <Name>WeightExpander</Name>
                <Text>Gewichte</Text>
                <Value>True</Value>
                <ValueType>Expander</ValueType>
                <Parameters>
                    <Parameter>
                        <Name>WeightPerLevel</Name>
                        <Text>Gewicht pro Ebene (kg)</Text>
                        <TextDyn>f"Ebene {$list_row + 1} (kg)"</TextDyn>
                        <Value>[1000.0, 1000.0, 800.0]</Value>
                        <ValueType>Double</ValueType>
                        <Dimensions>LevelCountZ</Dimensions>
                    </Parameter>
                </Parameters>
            </Parameter>
        </Parameters>
    </Page>

    <Page>
        <Name>PageDisplay</Name>
        <Text>Darstellung</Text>
        <Parameters>
            <Parameter>
                <Name>ColorPosts</Name>
                <Text>Farbe Stuetzen</Text>
                <Value>1</Value>
                <ValueType>Color</ValueType>
            </Parameter>
            <Parameter>
                <Name>PenPosts</Name>
                <Text>Stift Stuetzen</Text>
                <Value>1</Value>
                <ValueType>Pen</ValueType>
            </Parameter>
            <Parameter>
                <Name>DisplaySep1</Name>
                <Text></Text>
                <ValueType>Separator</ValueType>
            </Parameter>
            <Parameter>
                <Name>ColorBeams</Name>
                <Text>Farbe Traversen</Text>
                <Value>3</Value>
                <ValueType>Color</ValueType>
            </Parameter>
            <Parameter>
                <Name>PenBeams</Name>
                <Text>Stift Traversen</Text>
                <Value>1</Value>
                <ValueType>Pen</ValueType>
            </Parameter>
            <Parameter>
                <Name>DisplaySep2</Name>
                <Text></Text>
                <ValueType>Separator</ValueType>
            </Parameter>
            <Parameter>
                <Name>ColorShelves</Name>
                <Text>Farbe Boeden</Text>
                <Value>6</Value>
                <ValueType>Color</ValueType>
            </Parameter>
            <Parameter>
                <Name>PenShelves</Name>
                <Text>Stift Boeden</Text>
                <Value>1</Value>
                <ValueType>Pen</ValueType>
            </Parameter>
            <Parameter>
                <Name>DisplaySep3</Name>
                <Text></Text>
                <ValueType>Separator</ValueType>
            </Parameter>
            <Parameter>
                <Name>ColorBracing</Name>
                <Text>Farbe Diagonalen</Text>
                <Value>5</Value>
                <ValueType>Color</ValueType>
            </Parameter>
            <Parameter>
                <Name>PenBracing</Name>
                <Text>Stift Diagonalen</Text>
                <Value>1</Value>
                <ValueType>Pen</ValueType>
            </Parameter>
            <Parameter>
                <Name>DisplaySep4</Name>
                <Text></Text>
                <ValueType>Separator</ValueType>
            </Parameter>
            <Parameter>
                <Name>ColorBasePlates</Name>
                <Text>Farbe Fussplatten</Text>
                <Value>4</Value>
                <ValueType>Color</ValueType>
            </Parameter>
            <Parameter>
                <Name>PenBasePlates</Name>
                <Text>Stift Fussplatten</Text>
                <Value>1</Value>
                <ValueType>Pen</ValueType>
            </Parameter>
            <Parameter>
                <Name>DisplaySep5</Name>
                <Text></Text>
                <ValueType>Separator</ValueType>
            </Parameter>
            <Parameter>
                <Name>ColorPallets</Name>
                <Text>Farbe Paletten</Text>
                <Value>4</Value>
                <ValueType>Color</ValueType>
            </Parameter>
            <Parameter>
                <Name>PenPallets</Name>
                <Text>Stift Paletten</Text>
                <Value>1</Value>
                <ValueType>Pen</ValueType>
            </Parameter>
        </Parameters>
    </Page>

    <Page>
        <Name>PageInfo</Name>
        <Text>Info</Text>
        <Parameters>
            <Parameter>
                <Name>TotalLength</Name>
                <Text>Gesamtlaenge</Text>
                <Value>0</Value>
                <ValueType>Length</ValueType>
                <Enable>False</Enable>
            </Parameter>
            <Parameter>
                <Name>TotalDepth</Name>
                <Text>Gesamttiefe</Text>
                <Value>0</Value>
                <ValueType>Length</ValueType>
                <Enable>False</Enable>
            </Parameter>
            <Parameter>
                <Name>TotalHeight</Name>
                <Text>Gesamthoehe</Text>
                <Value>0</Value>
                <ValueType>Length</ValueType>
                <Enable>False</Enable>
            </Parameter>
            <Parameter>
                <Name>InfoSep1</Name>
                <Text></Text>
                <ValueType>Separator</ValueType>
            </Parameter>
            <Parameter>
                <Name>TotalWeight</Name>
                <Text>Gesamtgewicht (kg)</Text>
                <Value>0</Value>
                <ValueType>Double</ValueType>
                <Enable>False</Enable>
            </Parameter>
            <Parameter>
                <Name>MaxBeamLoad</Name>
                <Text>Max. Traversenlast (kg)</Text>
                <Value>0</Value>
                <ValueType>Double</ValueType>
                <Enable>False</Enable>
            </Parameter>
            <Parameter>
                <Name>TotalPalletSlots</Name>
                <Text>Palettenplaetze gesamt</Text>
                <Value>0</Value>
                <ValueType>Integer</ValueType>
                <Enable>False</Enable>
            </Parameter>
            <Parameter>
                <Name>InfoSep2</Name>
                <Text></Text>
                <ValueType>Separator</ValueType>
            </Parameter>
            <Parameter>
                <Name>OverloadWarning</Name>
                <Text>Status</Text>
                <Value>OK</Value>
                <ValueType>String</ValueType>
                <Enable>False</Enable>
            </Parameter>
        </Parameters>
    </Page>
</Element>
