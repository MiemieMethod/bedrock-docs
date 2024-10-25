# `@minecraft/server-editor-bindings`

> 文档版本：1.21.50.25

`@minecraft/server-editor-bindings`模块的`0.1.0-beta`版本，UUID为`8518d9c7-a1f5-4bf3-acc7-78e87df595fc`。该模块是script_api.@minecraft/server-editor-bindings.description

/// info | 依赖
该模块依赖于以下模块：

- `@minecraft/common`|`1.0.0`|`77ec12b4-1b2b-4c98-8d34-d1cd63f849d5`
- `@minecraft/server`|`1.17.0-beta`|`b26a4d4c-afdf-4690-88f8-931846312678`
///

## 对象

/// define
`editor`


///

```js
static read-only editor: MinecraftEditor;
```

/// html | div.result
//// define
`editor`：[`MinecraftEditor`](./minecrafteditor.md)

- script_api.@minecraft/server-editor-bindings.editor.description


////

///


/// define
`editorInternal`


///

```js
static read-only editorInternal: MinecraftEditorInternal;
```

/// html | div.result
//// define
`editorInternal`：[`MinecraftEditorInternal`](./minecrafteditorinternal.md)

- script_api.@minecraft/server-editor-bindings.editorinternal.description


////

///


## 类

|类|描述|
|---|---|
|[`BlockPalette`](./blockpalette.md)||
|[`BlockPaletteManager`](./blockpalettemanager.md)||
|[`BrushShapeManager`](./brushshapemanager.md)||
|[`ClipboardChangeAfterEvent`](./clipboardchangeafterevent.md)||
|[`ClipboardChangeAfterEventSignal`](./clipboardchangeaftereventsignal.md)||
|[`ClipboardItem`](./clipboarditem.md)||
|[`ClipboardManager`](./clipboardmanager.md)||
|[`CurrentThemeChangeAfterEvent`](./currentthemechangeafterevent.md)||
|[`CurrentThemeChangeAfterEventSignal`](./currentthemechangeaftereventsignal.md)||
|[`CurrentThemeColorChangeAfterEvent`](./currentthemecolorchangeafterevent.md)||
|[`CurrentThemeColorChangeAfterEventSignal`](./currentthemecolorchangeaftereventsignal.md)||
|[`Cursor`](./cursor.md)||
|[`CursorAttachmentPropertiesChangeAfterEvent`](./cursorattachmentpropertieschangeafterevent.md)||
|[`CursorAttachmentPropertyChangeAfterEventSignal`](./cursorattachmentpropertychangeaftereventsignal.md)||
|[`CursorPropertiesChangeAfterEvent`](./cursorpropertieschangeafterevent.md)||
|[`CursorPropertyChangeAfterEventSignal`](./cursorpropertychangeaftereventsignal.md)||
|[`DataStore`](./datastore.md)||
|[`DataStoreActionBarContainer`](./datastoreactionbarcontainer.md)||
|[`DataStoreActionContainer`](./datastoreactioncontainer.md)||
|[`DataStoreAfterEvents`](./datastoreafterevents.md)||
|[`DataStoreMenuContainer`](./datastoremenucontainer.md)||
|[`DataStoreModalToolActivationChangedEvent`](./datastoremodaltoolactivationchangedevent.md)||
|[`DataStoreModalToolActivationChangedEventSignal`](./datastoremodaltoolactivationchangedeventsignal.md)||
|[`DataStoreModalToolContainer`](./datastoremodaltoolcontainer.md)||
|[`DataStorePayloadAfterEvent`](./datastorepayloadafterevent.md)||
|[`DataStorePayloadAfterEventSignal`](./datastorepayloadaftereventsignal.md)||
|[`DataTransferManager`](./datatransfermanager.md)||
|[`DataTransferRequestResponse`](./datatransferrequestresponse.md)||
|[`EditorStructureManager`](./editorstructuremanager.md)||
|[`ExportManager`](./exportmanager.md)||
|[`Extension`](./extension.md)||
|[`ExtensionContext`](./extensioncontext.md)||
|[`ExtensionContextAfterEvents`](./extensioncontextafterevents.md)||
|[`GraphicsSettings`](./graphicssettings.md)||
|[`IBlockPaletteItem`](./iblockpaletteitem.md)||
|[`InputService`](./inputservice.md)||
|[`InternalPlayerServiceContext`](./internalplayerservicecontext.md)||
|[`Logger`](./logger.md)||
|[`MinecraftEditor`](./minecrafteditor.md)||
|[`MinecraftEditorInternal`](./minecrafteditorinternal.md)||
|[`ModeChangeAfterEvent`](./modechangeafterevent.md)||
|[`ModeChangeAfterEventSignal`](./modechangeaftereventsignal.md)||
|[`PlaytestManager`](./playtestmanager.md)||
|[`PrimarySelectionChangeAfterEventSignal`](./primaryselectionchangeaftereventsignal.md)||
|[`PrimarySelectionChangedEvent`](./primaryselectionchangedevent.md)||
|[`ProbabilityBlockPaletteItem`](./probabilityblockpaletteitem.md)||
|[`Selection`](./selection.md)||
|[`SelectionEventAfterEvent`](./selectioneventafterevent.md)||
|[`SelectionManager`](./selectionmanager.md)||
|[`SettingsManager`](./settingsmanager.md)||
|[`SettingsUIElement`](./settingsuielement.md)||
|[`SimpleBlockPaletteItem`](./simpleblockpaletteitem.md)||
|[`SimulationState`](./simulationstate.md)||
|[`ThemeSettings`](./themesettings.md)||
|[`TickingAreaManager`](./tickingareamanager.md)||
|[`TransactionManager`](./transactionmanager.md)||
|[`UserDefinedTransactionHandlerId`](./userdefinedtransactionhandlerid.md)||
|[`Widget`](./widget.md)||
|[`WidgetComponentBase`](./widgetcomponentbase.md)||
|[`WidgetComponentEntity`](./widgetcomponententity.md)||
|[`WidgetComponentGizmo`](./widgetcomponentgizmo.md)||
|[`WidgetComponentGuide`](./widgetcomponentguide.md)||
|[`WidgetComponentRenderPrimitive`](./widgetcomponentrenderprimitive.md)||
|[`WidgetComponentRenderPrimitiveAxialSphere`](./widgetcomponentrenderprimitiveaxialsphere.md)||
|[`WidgetComponentRenderPrimitiveBox`](./widgetcomponentrenderprimitivebox.md)||
|[`WidgetComponentRenderPrimitiveDisc`](./widgetcomponentrenderprimitivedisc.md)||
|[`WidgetComponentRenderPrimitiveLine`](./widgetcomponentrenderprimitiveline.md)||
|[`WidgetComponentSpline`](./widgetcomponentspline.md)||
|[`WidgetComponentText`](./widgetcomponenttext.md)||
|[`WidgetGroup`](./widgetgroup.md)||
|[`WidgetManager`](./widgetmanager.md)||
|[`WidgetMouseButtonEventData`](./widgetmousebuttoneventdata.md)||
|[`WidgetStateChangeEventData`](./widgetstatechangeeventdata.md)||

## 接口

|接口|描述|
|---|---|
|[`BlockMaskList`](./blockmasklist.md)||
|[`BrushShape`](./brushshape.md)||
|[`ClipboardWriteOptions`](./clipboardwriteoptions.md)||
|[`CursorAttachmentProperties`](./cursorattachmentproperties.md)||
|[`CursorProperties`](./cursorproperties.md)||
|[`DataTransferCollectionNameData`](./datatransfercollectionnamedata.md)||
|[`EditorStructure`](./editorstructure.md)||
|[`EditorStructureSearchOptions`](./editorstructuresearchoptions.md)||
|[`ExtensionOptionalParameters`](./extensionoptionalparameters.md)||
|[`GameOptions`](./gameoptions.md)||
|[`InputBindingInfo`](./inputbindinginfo.md)||
|[`LogProperties`](./logproperties.md)||
|[`ProjectExportOptions`](./projectexportoptions.md)||
|[`SettingsUIElementOptions`](./settingsuielementoptions.md)||
|[`WeightedBlock`](./weightedblock.md)||
|[`WidgetComponentBaseOptions`](./widgetcomponentbaseoptions.md)||
|[`WidgetComponentEntityOptions`](./widgetcomponententityoptions.md)||
|[`WidgetComponentGizmoOptions`](./widgetcomponentgizmooptions.md)||
|[`WidgetComponentGuideOptions`](./widgetcomponentguideoptions.md)||
|[`WidgetComponentRenderPrimitiveOptions`](./widgetcomponentrenderprimitiveoptions.md)||
|[`WidgetComponentSplineOptions`](./widgetcomponentsplineoptions.md)||
|[`WidgetComponentTextOptions`](./widgetcomponenttextoptions.md)||
|[`WidgetCreateOptions`](./widgetcreateoptions.md)||
|[`WidgetGroupCreateOptions`](./widgetgroupcreateoptions.md)||

## 枚举

|枚举|描述|
|---|---|
|[`BlockMaskListType`](./blockmasklisttype.md)||
|[`BlockPaletteItemType`](./blockpaletteitemtype.md)||
|[`BrushShapeType`](./brushshapetype.md)||
|[`CursorControlMode`](./cursorcontrolmode.md)||
|[`CursorTargetMode`](./cursortargetmode.md)||
|[`DaylightCycle`](./daylightcycle.md)||
|[`EditorMode`](./editormode.md)||
|[`EntityOperationType`](./entityoperationtype.md)||
|[`ExportResult`](./exportresult.md)||
|[`GamePublishSetting`](./gamepublishsetting.md)||
|[`GraphicsSettingsProperty`](./graphicssettingsproperty.md)||
|[`InputModifier`](./inputmodifier.md)||
|[`KeyInputType`](./keyinputtype.md)||
|[`PaintCompletionState`](./paintcompletionstate.md)||
|[`PaintMode`](./paintmode.md)||
|[`Plane`](./plane.md)||
|[`PlayerPermissionLevel`](./playerpermissionlevel.md)||
|[`PlaytestSessionResult`](./playtestsessionresult.md)||
|[`PrimitiveType`](./primitivetype.md)||
|[`ProjectExportType`](./projectexporttype.md)||
|[`SplineType`](./splinetype.md)||
|[`ThemeSettingsColorKey`](./themesettingscolorkey.md)||
|[`WidgetComponentType`](./widgetcomponenttype.md)||
|[`WidgetGroupSelectionMode`](./widgetgroupselectionmode.md)||
|[`WidgetMouseButtonActionType`](./widgetmousebuttonactiontype.md)||

## 错误

|错误|描述|
|---|---|
|[`InvalidWidgetComponentError`](./invalidwidgetcomponenterror.md)||
|[`InvalidWidgetError`](./invalidwidgeterror.md)||
|[`InvalidWidgetGroupError`](./invalidwidgetgrouperror.md)||
