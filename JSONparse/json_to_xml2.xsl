<?xml version="1.0" encoding="utf-8"?>
<xsl:stylesheet version="2.0" 
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:fn="http://www.w3.org/2005/xpath-functions"
    xmlns:xs="http://www.w3.org/2001/XMLSchema">
    
    <xsl:output indent="yes"/>
    
    <xsl:template match="/*:Расширение_МСЭ">
        
        <xsl:variable name="расширение_МСЭ">
            <xsl:value-of select="*:value"/>
        </xsl:variable>
        <!-- Вывод всех value -->
        <!--<xsl:value-of select="$расширение_МСЭ//*:string/following-sibling::*:string"/>-->
        <!-- only for XSLT 3.0-->
        <!--<xsl:for-each select="$расширение_МСЭ//*:string">
            <xsl:if test="text() = 'nationality'">
                <xsl:value-of select="following-sibling::*:string"/>
            </xsl:if>
        </xsl:for-each>-->
        
        <!--<xsl:value-of select="$расширение_МСЭ//following-sibling::*:string"/>-->
        
        <xsl:variable name="codes">
            <xsl:analyze-string select="$расширение_МСЭ" regex="&quot;code&quot;[ :][ ]*(&quot;.*?&quot;)">
            <xsl:matching-substring>
                <xsl:value-of select="regex-group(1)"/>
            </xsl:matching-substring>
        </xsl:analyze-string>
        </xsl:variable>
        
        <xsl:variable name="values">
            <xsl:analyze-string select="$расширение_МСЭ" regex="&quot;value&quot;[ :][ ]*(&quot;.*?&quot;)">
                <xsl:matching-substring>
<!--                        <xsl:copy-of select="replace(regex-group(1), '&quot;','')"/>-->
                    <xsl:value-of select="regex-group(1)"/>
                </xsl:matching-substring>
            </xsl:analyze-string>
        </xsl:variable>
        
        <xsl:variable name="valuesList">
            <xsl:for-each select="tokenize(normalize-space($values),'&quot;&quot;')">
                <item>
                    <xsl:copy-of select="replace(., '&quot;','')"/>
                </item>
            </xsl:for-each>
        </xsl:variable>
        
        <xsl:variable name="codesList">
            <xsl:for-each select="tokenize(normalize-space($codes), '&quot;&quot;')">
                <item>
                    <xsl:copy-of select="replace(., '&quot;','')"/>
                </item>
            </xsl:for-each>
        </xsl:variable>
        
       <!-- <xsl:copy-of select="$valuesList"/>
        <xsl:copy-of select="$codesList"/>-->
        
        <xsl:for-each select="$codesList/*:item">
            
                <xsl:copy-of select="."/>
        
        </xsl:for-each>
    </xsl:template>
    
    
</xsl:stylesheet>
