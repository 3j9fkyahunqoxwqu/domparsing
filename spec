<!DOCTYPE html><meta charset=UTF-8>
<title>Spec</title>
<link href=http://www.whatwg.org/style/specification rel=stylesheet>
<style>
 pre, code { font-family:monospace, sans-serif; }
 h2 code, h3 code, h4 code,
 h2 :link, h3 :link, h4 :link,
 h2 :visited, h3 :visited, h4 :visited
 { font:inherit; color:inherit; font-style:italic; }
 @media print {
   [data-anolis-spec]::after {
     content: "[" attr(data-anolis-spec) "]";
     font-size: 0.6em;
     vertical-align: super;
     text-transform: uppercase;
   }
 }
</style>
<body class=draft>
<div class=head id=head>
<h1>Spec</h1>
<h2 class="no-num no-toc" id=work-in-progress-&mdash;-last-update-3-september-2010>Work in Progress &mdash; Last Update 3 September 2010</h2>
<dl>
 <dt>Editor
 <dd>Ms2ger &lt;ms2ger@gmail.com&gt;

 <dt>Version history
 <dd><a href=http://bitbucket.org/ms2ger/repo/>http://bitbucket.org/ms2ger/repo</a>
</dl>
</div>



<h2 class="no-num no-toc" id=abstract>Abstract</h2>
<p>



<h2 class="no-num no-toc" id=table-of-contents>Table of contents</h2>

<!--begin-toc-->
<ol class=toc>
 <li><a href=#common-infrastructure><span class=secno>1 </span>Common infrastructure</a>
  <ol>
   <li><a href=#terminology><span class=secno>1.1 </span>Terminology</a></li>
   <li><a href=#conformance-requirements><span class=secno>1.2 </span>Conformance requirements</a>
    <ol>
     <li><a href=#dependencies><span class=secno>1.2.1 </span>Dependencies</a></li>
     <li><a href=#extensibility><span class=secno>1.2.2 </span>Extensibility</a></ol></ol></li>
 <li><a class=no-num href=#references>References</a></li>
 <li><a class=no-num href=#acknowledgements>Acknowledgements</a></ol>
<!--end-toc-->



<h2 id=common-infrastructure><span class=secno>1 </span>Common infrastructure</h2>
<h3 id=terminology><span class=secno>1.1 </span>Terminology</h3>
<p>


<h3 id=conformance-requirements><span class=secno>1.2 </span>Conformance requirements</h3>
<p>All diagrams, examples, and notes in this specification are
non-normative, as are all sections explicitly marked non-normative.
Everything else in this specification is normative.</p>

<p>The key words "MUST", "MUST NOT", "REQUIRED", <!--"SHALL", "SHALL
NOT",--> "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and
"OPTIONAL" in the normative parts of this document are to be
interpreted as described in RFC2119. For readability, these words do
not appear in all uppercase letters in this specification. <a data-anolis-ref="" href=#refsRFC2119>[RFC2119]</a></p>

<p>Requirements phrased in the imperative as part of algorithms
(such as "strip any leading space characters" or "return false and
abort these steps") are to be interpreted with the meaning of the
key word ("must", "should", "may", etc) used in introducing the
algorithm.</p>

<p>Conformance requirements phrased as algorithms or specific steps
may be implemented in any manner, so long as the end result is
equivalent. (In particular, the algorithms defined in this
specification are intended to be easy to follow, and not intended to
be performant.)</p>

<p id=hardwareLimitations>User agents may impose
implementation-specific limits on otherwise unconstrained inputs,
e.g. to prevent denial of service attacks, to guard against running
out of memory, or to work around platform-specific limitations.</p>

<p>When a method or an attribute is said to call another method or attribute, the user agent must invoke its internal API for that attribute or method so that e.g. the author can't change the behavior by overriding attributes or methods with custom properties or functions in ECMAScript.

<p>Unless otherwise stated, string comparisons are done in a <span>case-sensitive</span> manner.

<h4 id=dependencies><span class=secno>1.2.1 </span>Dependencies</h4>

<p>The IDL fragments in this specification must be interpreted as
required for conforming IDL fragments, as described in the Web IDL
specification. <a data-anolis-ref="" href=#refsWEBIDL>[WEBIDL]</a>

<p id=float-nan>Except where otherwise specified, if an IDL attribute that is a
floating point number type (<a href=http://dev.w3.org/2006/webapi/WebIDL/#idl-float><code class=external data-anolis-spec=webidl>float</code></a>) is
assigned an Infinity or Not-a-Number (NaN) value, a <code title=dom-DOMException-NOT_SUPPORTED_ERR>NOT_SUPPORTED_ERR</code> exception must
be raised.

<p>Except where otherwise specified, if a method with an argument that is a
floating point number type (<a href=http://dev.w3.org/2006/webapi/WebIDL/#idl-float><code class=external data-anolis-spec=webidl>float</code></a>) is
passed an Infinity or Not-a-Number (NaN) value, a <code title=dom-DOMException-NOT_SUPPORTED_ERR>NOT_SUPPORTED_ERR</code> exception must
be raised.

<p>Some of the terms used in this specification are defined in <cite>Web
IDL</cite>, <cite>XML</cite>, <cite>Namespaces in XML</cite> and
<cite>HTML</cite>. <a data-anolis-ref="" href=#refsWEBIDL>[WEBIDL]</a> <a data-anolis-ref="" href=#refsXML>[XML]</a> <a data-anolis-ref="" href=#refsXMLNS>[XMLNS]</a> <a data-anolis-ref="" href=#refsHTML>[HTML]</a>

<h4 id=extensibility><span class=secno>1.2.2 </span>Extensibility</h4>

<p>Vendor-specific proprietary extensions to this specification are
strongly discouraged. Authors must not use such extensions, as
doing so reduces interoperability and fragments the user base,
allowing only users of specific user agents to access the content in
question.</p>

<p>If vendor-specific extensions are needed, the members should be
prefixed by vendor-specific strings to prevent clashes with future
versions of this specification. Extensions must be defined so that
the use of extensions neither contradicts nor causes the
non-conformance of functionality defined in the specification.</p>
<!-- thanks to QA Framework -->

<p>When vendor-neutral extensions to this specification are needed,
either this specification can be updated accordingly, or an
extension specification can be written that overrides the
requirements in this specification. When someone applying this
specification to their activities decides that they will recognise
the requirements of such an extension specification, it becomes an
<dfn id=other-applicable-specifications title="other applicable specifications">applicable
specification</dfn> for the purposes of conformance requirements in
this specification.</p>
<!-- http://www.w3.org/mid/17E341CD-E790-422C-9F9A-69347EE01CEB@iki.fi -->


<h2 class=no-num id=references>References</h2><!--REFS-->
<p>All references are normative unless marked "Non-normative".</p>

<!-- Dates are only included for standards older than the Web,
because the newer ones keep changing. -->

<div id=anolis-references><dl><dt id=refsHTML>[HTML]
<dd><cite><a href=http://www.whatwg.org/specs/web-apps/current-work/multipage>HTML</a></cite>, I. Hickson. WHATWG.
<dt id=refsRFC2119>[RFC2119]
<dd><cite><a href=http://www.ietf.org/rfc/rfc2119.txt>Key words for use in RFCs to Indicate Requirement Levels</a></cite>, S. Bradner. IETF.
<dt id=refsWEBIDL>[WEBIDL]
<dd><cite><a href=http://dev.w3.org/2006/webapi/WebIDL/>Web IDL</a></cite>, C. McCormack, S. Weinig. W3C.
<dt id=refsXML>[XML]
<dd><cite><a href=http://www.w3.org/TR/xml/>Extensible Markup Language</a></cite>, T. Bray, J. Paoli, C. Sperberg-McQueen, E. Maler, F. Yergeau. W3C.
<dt id=refsXMLNS>[XMLNS]
<dd><cite><a href=http://www.w3.org/TR/xml-names/>Namespaces in XML</a></cite>, T. Bray, D. Hollander, A. Layman, R. Tobin. W3C.
</dl></div>



<h2 class=no-num id=acknowledgements>Acknowledgements</h2>
<p>Thanks to



for their useful comments.


<script src=http://www.whatwg.org/specs/web-apps/current-work/dfn.js></script>
