<template>
  <div
    jscontroller="Y9IaVe"
    jsaction=""
    jsname="dWPKW"
    class="d2CFce cDSmF cxMOTc"
    data-allow-at-sign="true"
    role="presentation"
    data-is-rendered="true"
    v-bind:style="style"
  >
    <div
      :class="inputContainerClass.current"
      jscontroller="pxq3x"
      jsaction="clickonly:KjsqPd; focus:Jt1EX; blur:fpfTEe; input:Lg5SV"
      jsshadow=""
      jsname="Vsb5Ub"
    >
      <div class="aCsJod oJeWuf">
        <div class="aXBtI Wic03c">
          
          <span v-if="withGSpan" data-v-3b8fca39="" jsslot="" class="A37UZe qgcB3c iHd5yb">G-</span>
          
          <div class="Xb9hP">
            <input
              
              @focus="onFocus"
              @blur="onBlur"
              :type="type"
              class="whsOnd zHQkBf"
              jsname="YPqjbf"
              spellcheck="false"
              tabindex="0"
              :aria-label="placeHolder"
              name="identifier"
              autocapitalize="none"
              id="identifierId"
              dir="ltr"
              data-initial-dir="ltr"
              data-initial-value=""
              badinput="false"
              v-model="enteredText"
              v-bind:value="enteredText"
              v-on:input="$emit('input', $event.target.value)"
              :autocomplete="autoComplete"
            />
            <div jsname="YRMmle" class="AxOyFc snByac" aria-hidden="true">
              {{ placeHolder }}
            </div>
          </div>
          <div class="i9lrp mIZh1c"></div>
          <div
            jsname="XmnwAc"
            class="OabDMe cXrdqd Y2Zypf"
            style="transform-origin: 278px center"
          ></div>
        </div>
      </div>
      <div class="LXRPh">
        <div jsname="ty6ygf" class="ovnfwe Is7Fhb"></div>
        <div
          jsname="B34EJ"
          class="dEOOab RxsGPe"
          aria-atomic="true"
          aria-live="assertive"
        ></div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    type: String,
    placeholder: String,
    withGSpan: Boolean,
    autoComplete: String
  },
  data() {
    return {
      placeHolder: "",
      enteredText: '',
      style: {
        "margin-top": (this.type == 'password') ? '15px' : '',
      },
      inputContainerClass: {
        onBlur: "rFrNMe N3Hzgf jjwyfe QBQrY zKHdkd sdJrJc Tyc9J",
        current: "rFrNMe N3Hzgf jjwyfe QBQrY zKHdkd sdJrJc Tyc9J",
        onWriting: "rFrNMe N3Hzgf jjwyfe QBQrY zKHdkd sdJrJc Tyc9J u3bW4e"
      }
    }
  },
  methods: {
    /*onChange() {
      console.log(this.enteredText)
      if (this.enteredText !== '') {
        const onWritingClass = this.inputContainerClass.onWriting
        this.inputContainerClass.current = onWritingClass
      } 
    }*/
    onFocus() {
      this.inputContainerClass.current = this.inputContainerClass.onWriting
      this.placeHolder = this.placeholder
    },
    onBlur() {
      if (this.enteredText !== '') {
        this.placeHolder = ""
      }
      this.inputContainerClass.current = this.inputContainerClass.onBlur
    }
    
  },
  mounted() {
    this.placeHolder = this.placeholder
  }
}
</script>

<style scoped>
</style>