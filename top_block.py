#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Sun Jun  2 00:29:05 2019
##################################################


if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.wxgui import forms
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import wx


class top_block(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Top Block")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.variable_slider_Audio_level_0 = variable_slider_Audio_level_0 = 1
        self.variable_slider_Audio_level = variable_slider_Audio_level = 1
        self.variable_slider_0 = variable_slider_0 = 2.400140e9
        self.samp_rate = samp_rate = 2e6
        self.rf_gain = rf_gain = 100
        self.modelation_amp = modelation_amp = 1
        self.mixer_level = mixer_level = 1
        self.if_gain = if_gain = 100
        self.bb_gain = bb_gain = 59
        self.Audio_freq = Audio_freq = 1000

        ##################################################
        # Blocks
        ##################################################
        _variable_slider_Audio_level_0_sizer = wx.BoxSizer(wx.VERTICAL)
        self._variable_slider_Audio_level_0_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_variable_slider_Audio_level_0_sizer,
        	value=self.variable_slider_Audio_level_0,
        	callback=self.set_variable_slider_Audio_level_0,
        	label='Modulator amp',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._variable_slider_Audio_level_0_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_variable_slider_Audio_level_0_sizer,
        	value=self.variable_slider_Audio_level_0,
        	callback=self.set_variable_slider_Audio_level_0,
        	minimum=0,
        	maximum=10,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.GridAdd(_variable_slider_Audio_level_0_sizer, 0, 1, 1, 1)
        _mixer_level_sizer = wx.BoxSizer(wx.VERTICAL)
        self._mixer_level_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_mixer_level_sizer,
        	value=self.mixer_level,
        	callback=self.set_mixer_level,
        	label='Mixer Level',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._mixer_level_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_mixer_level_sizer,
        	value=self.mixer_level,
        	callback=self.set_mixer_level,
        	minimum=0,
        	maximum=5,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.GridAdd(_mixer_level_sizer, 1, 1, 1, 1)
        _variable_slider_Audio_level_sizer = wx.BoxSizer(wx.VERTICAL)
        self._variable_slider_Audio_level_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_variable_slider_Audio_level_sizer,
        	value=self.variable_slider_Audio_level,
        	callback=self.set_variable_slider_Audio_level,
        	label='Audio Level',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._variable_slider_Audio_level_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_variable_slider_Audio_level_sizer,
        	value=self.variable_slider_Audio_level,
        	callback=self.set_variable_slider_Audio_level,
        	minimum=0,
        	maximum=2,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.GridAdd(_variable_slider_Audio_level_sizer, 1, 2, 1, 1)
        _variable_slider_0_sizer = wx.BoxSizer(wx.VERTICAL)
        self._variable_slider_0_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_variable_slider_0_sizer,
        	value=self.variable_slider_0,
        	callback=self.set_variable_slider_0,
        	label='TX Frequency',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._variable_slider_0_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_variable_slider_0_sizer,
        	value=self.variable_slider_0,
        	callback=self.set_variable_slider_0,
        	minimum=2.400e9,
        	maximum=2.40035e9,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.GridAdd(_variable_slider_0_sizer, 1, 3, 1, 1)
        _rf_gain_sizer = wx.BoxSizer(wx.VERTICAL)
        self._rf_gain_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_rf_gain_sizer,
        	value=self.rf_gain,
        	callback=self.set_rf_gain,
        	label='RF Gain',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._rf_gain_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_rf_gain_sizer,
        	value=self.rf_gain,
        	callback=self.set_rf_gain,
        	minimum=1,
        	maximum=100,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.GridAdd(_rf_gain_sizer, 0, 3, 1, 1)
        self.rational_resampler_xxx_1 = filter.rational_resampler_ccc(
                interpolation=2000000,
                decimation=192000,
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_0 = filter.rational_resampler_fff(
                interpolation=24,
                decimation=6,
                taps=None,
                fractional_bw=None,
        )
        _modelation_amp_sizer = wx.BoxSizer(wx.VERTICAL)
        self._modelation_amp_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_modelation_amp_sizer,
        	value=self.modelation_amp,
        	callback=self.set_modelation_amp,
        	label='modelation Amp',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._modelation_amp_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_modelation_amp_sizer,
        	value=self.modelation_amp,
        	callback=self.set_modelation_amp,
        	minimum=0.1,
        	maximum=10,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.GridAdd(_modelation_amp_sizer, 2, 1, 1, 1)
        self.low_pass_filter_0 = filter.fir_filter_ccf(1, firdes.low_pass(
        	1, 192000, 3500, 1000, firdes.WIN_HAMMING, 6.76))
        _if_gain_sizer = wx.BoxSizer(wx.VERTICAL)
        self._if_gain_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_if_gain_sizer,
        	value=self.if_gain,
        	callback=self.set_if_gain,
        	label='if_gain',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._if_gain_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_if_gain_sizer,
        	value=self.if_gain,
        	callback=self.set_if_gain,
        	minimum=1,
        	maximum=100,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_if_gain_sizer)
        self.hilbert_fc_0 = filter.hilbert_fc(256, firdes.WIN_HAMMING, 6.76)
        (self.hilbert_fc_0).set_min_output_buffer(10)
        (self.hilbert_fc_0).set_max_output_buffer(10)
        self.blocks_wavfile_source_0 = blocks.wavfile_source('/home/anton/gnuradio-grc-examples/test_audio.wav', True)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_float*1, 48e3,True)
        self.blocks_null_sink_0 = blocks.null_sink(gr.sizeof_gr_complex*1)
        self.blocks_multiply_xx_0_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_const_vxx_0_0 = blocks.multiply_const_vcc((variable_slider_Audio_level_0, ))
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((variable_slider_Audio_level_0, ))
        _bb_gain_sizer = wx.BoxSizer(wx.VERTICAL)
        self._bb_gain_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_bb_gain_sizer,
        	value=self.bb_gain,
        	callback=self.set_bb_gain,
        	label='BB Gain',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._bb_gain_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_bb_gain_sizer,
        	value=self.bb_gain,
        	callback=self.set_bb_gain,
        	minimum=1,
        	maximum=59,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.GridAdd(_bb_gain_sizer, 2, 2, 1, 1)
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, 192e3, mixer_level, 0)
        _Audio_freq_sizer = wx.BoxSizer(wx.VERTICAL)
        self._Audio_freq_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_Audio_freq_sizer,
        	value=self.Audio_freq,
        	callback=self.set_Audio_freq,
        	label='Audio freq',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._Audio_freq_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_Audio_freq_sizer,
        	value=self.Audio_freq,
        	callback=self.set_Audio_freq,
        	minimum=100,
        	maximum=2000,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.GridAdd(_Audio_freq_sizer, 0, 2, 1, 1)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.blocks_null_sink_0, 0))
        self.connect((self.blocks_multiply_xx_0_0, 0), (self.rational_resampler_xxx_1, 0))
        self.connect((self.blocks_throttle_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.blocks_wavfile_source_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.hilbert_fc_0, 0), (self.low_pass_filter_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.blocks_multiply_xx_0_0, 1))
        self.connect((self.rational_resampler_xxx_0, 0), (self.hilbert_fc_0, 0))
        self.connect((self.rational_resampler_xxx_1, 0), (self.blocks_multiply_const_vxx_0_0, 0))

    def get_variable_slider_Audio_level_0(self):
        return self.variable_slider_Audio_level_0

    def set_variable_slider_Audio_level_0(self, variable_slider_Audio_level_0):
        self.variable_slider_Audio_level_0 = variable_slider_Audio_level_0
        self._variable_slider_Audio_level_0_slider.set_value(self.variable_slider_Audio_level_0)
        self._variable_slider_Audio_level_0_text_box.set_value(self.variable_slider_Audio_level_0)
        self.blocks_multiply_const_vxx_0_0.set_k((self.variable_slider_Audio_level_0, ))
        self.blocks_multiply_const_vxx_0.set_k((self.variable_slider_Audio_level_0, ))

    def get_variable_slider_Audio_level(self):
        return self.variable_slider_Audio_level

    def set_variable_slider_Audio_level(self, variable_slider_Audio_level):
        self.variable_slider_Audio_level = variable_slider_Audio_level
        self._variable_slider_Audio_level_slider.set_value(self.variable_slider_Audio_level)
        self._variable_slider_Audio_level_text_box.set_value(self.variable_slider_Audio_level)

    def get_variable_slider_0(self):
        return self.variable_slider_0

    def set_variable_slider_0(self, variable_slider_0):
        self.variable_slider_0 = variable_slider_0
        self._variable_slider_0_slider.set_value(self.variable_slider_0)
        self._variable_slider_0_text_box.set_value(self.variable_slider_0)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)

    def get_rf_gain(self):
        return self.rf_gain

    def set_rf_gain(self, rf_gain):
        self.rf_gain = rf_gain
        self._rf_gain_slider.set_value(self.rf_gain)
        self._rf_gain_text_box.set_value(self.rf_gain)

    def get_modelation_amp(self):
        return self.modelation_amp

    def set_modelation_amp(self, modelation_amp):
        self.modelation_amp = modelation_amp
        self._modelation_amp_slider.set_value(self.modelation_amp)
        self._modelation_amp_text_box.set_value(self.modelation_amp)

    def get_mixer_level(self):
        return self.mixer_level

    def set_mixer_level(self, mixer_level):
        self.mixer_level = mixer_level
        self._mixer_level_slider.set_value(self.mixer_level)
        self._mixer_level_text_box.set_value(self.mixer_level)
        self.analog_sig_source_x_0.set_amplitude(self.mixer_level)

    def get_if_gain(self):
        return self.if_gain

    def set_if_gain(self, if_gain):
        self.if_gain = if_gain
        self._if_gain_slider.set_value(self.if_gain)
        self._if_gain_text_box.set_value(self.if_gain)

    def get_bb_gain(self):
        return self.bb_gain

    def set_bb_gain(self, bb_gain):
        self.bb_gain = bb_gain
        self._bb_gain_slider.set_value(self.bb_gain)
        self._bb_gain_text_box.set_value(self.bb_gain)

    def get_Audio_freq(self):
        return self.Audio_freq

    def set_Audio_freq(self, Audio_freq):
        self.Audio_freq = Audio_freq
        self._Audio_freq_slider.set_value(self.Audio_freq)
        self._Audio_freq_text_box.set_value(self.Audio_freq)


def main(top_block_cls=top_block, options=None):

    tb = top_block_cls()
    tb.Start(True)
    tb.Wait()


if __name__ == '__main__':
    main()
